"""Import past FS Quiz problems into coach/competitions/<event>/problems/<question_id>/.

Re-runnable: problems people verified or locked are never touched, fields topic
checkers own are kept, and solution.md is only refreshed while it still carries the
import marker.
"""

from dataclasses import dataclass, field
from pathlib import Path

from . import convert
from .client import NotFound


@dataclass
class ImportReport:
    problems_written: int = 0
    problems_unchanged: int = 0
    problems_protected: int = 0
    solutions_written: int = 0
    images_downloaded: int = 0
    quizzes_imported: int = 0
    quizzes_skipped: int = 0
    problems_per_event: dict = field(default_factory=dict)
    events_imported: list = field(default_factory=list)
    events_left_out: list = field(default_factory=list)
    warnings: list = field(default_factory=list)


def event_matches(event, names):
    """A config entry names an event by its exact short name ("FSG") or by part of its
    full name ("Alpe Adria"), ignoring case."""
    short_name = event["short_name"].lower()
    event_name = (event.get("event_name") or "").lower()
    return any(name.lower() == short_name or name.lower() in event_name for name in names)


def selected_events(events, config):
    """Events to import with their competition folder, as (event, folder) pairs."""
    only_events = config.get("events") or []
    skip_events = config.get("skip_events") or []
    folder_names = config.get("folder_names") or {}
    chosen = []
    for event in events:
        if only_events and not event_matches(event, only_events):
            continue
        if event_matches(event, skip_events):
            continue
        chosen.append((event, convert.event_folder(event, folder_names)))
    return chosen


def event_label(event):
    return event["short_name"] + " (" + (event.get("event_name") or "") + ")"


def quizzes_by_id(events_with_folders, quiz_statuses, report):
    """quiz_id -> (quiz summary, set of folders). One quiz can serve several events."""
    quizzes = {}
    for event, folder in events_with_folders:
        for quiz in event.get("quizzes") or []:
            if quiz.get("status") not in quiz_statuses:
                report.quizzes_skipped += 1
                continue
            quiz_id = convert.as_int(quiz["quiz_id"])
            summary, folders = quizzes.setdefault(quiz_id, (quiz, set()))
            folders.add(folder)
    return quizzes


def collect_problems(client, quizzes, report):
    """(folder, question_id) -> {"question": ..., "refs": [...]} over every chosen quiz."""
    problems = {}
    for quiz_id in sorted(quizzes):
        summary, folders = quizzes[quiz_id]
        try:
            quiz = client.get_json("quiz/" + str(quiz_id))
        except NotFound:
            report.warnings.append("quiz " + str(quiz_id) + " not found")
            continue
        report.quizzes_imported += 1
        # The quiz summary from /event/all has the year and class even if the detail lacks them.
        quiz = dict(summary, **{key: value for key, value in quiz.items() if value is not None})
        for question in quiz.get("questions") or []:
            question_id = convert.as_int(question["question_id"])
            reference = convert.quiz_reference(quiz, question.get("position_index"))
            for folder in sorted(folders):
                entry = problems.setdefault((folder, question_id), {"question": question, "refs": []})
                if all(ref["quiz_id"] != reference["quiz_id"] for ref in entry["refs"]):
                    entry["refs"].append(reference)
    return problems


def read_existing_fields(problem_file):
    if not problem_file.exists():
        return None
    fields, _ = convert.parse_front_matter(problem_file.read_text(encoding="utf-8"))
    return fields


def write_if_changed(path, content):
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def download_images(client, problem_dir, image_paths, inline_image_urls, report):
    downloads = [(convert.image_url(path), convert.image_file_name(path)) for path in image_paths]
    downloads += [(url, convert.image_file_name(url)) for url in inline_image_urls]
    for url, file_name in downloads:
        try:
            if client.download(url, problem_dir / "images" / file_name):
                report.images_downloaded += 1
        except Exception as error:  # one broken image must not stop the whole import
            report.warnings.append("image " + url + ": " + str(error))


def write_problem(client, problem_dir, folder, question, refs, topics, report):
    problem_file = problem_dir / "problem.md"
    existing_fields = read_existing_fields(problem_file)
    if convert.is_protected(existing_fields):
        report.problems_protected += 1
        return
    question_id = convert.as_int(question["question_id"])
    text_markdown, inline_image_urls = convert.to_markdown(question.get("text"))
    image_paths = [image["path"] for image in question.get("images") or []]
    fields = convert.problem_fields(question, folder, refs, topics, existing_fields)
    image_names = [convert.image_file_name(path) for path in image_paths]
    body = convert.problem_body(question_id, text_markdown, image_names, fields["options"])
    if write_if_changed(problem_file, convert.render_problem(fields, body)):
        report.problems_written += 1
    else:
        report.problems_unchanged += 1
    download_images(client, problem_dir, image_paths, inline_image_urls, report)

    # The API spec calls it "solutions", the live API answers with "solution".
    solutions = question.get("solution") or question.get("solutions")
    solution_text, solution_images, solution_inline_urls = convert.solution_markdown(question_id, solutions)
    if solution_text is None:
        return
    solution_file = problem_dir / "solution.md"
    hand_edited = solution_file.exists() and not solution_file.read_text(encoding="utf-8").startswith(convert.IMPORTED_MARKER)
    if hand_edited:
        return
    if write_if_changed(solution_file, solution_text):
        report.solutions_written += 1
    download_images(client, problem_dir, solution_images, solution_inline_urls, report)


def import_problems(client, coach_dir, config, log=print):
    report = ImportReport()
    events = client.get_json("event/all").get("events") or []
    events_with_folders = selected_events(events, config)
    chosen_ids = {event["id"] for event, _ in events_with_folders}
    report.events_imported = [event_label(event) + " -> " + folder for event, folder in events_with_folders]
    report.events_left_out = [event_label(event) for event in events if event["id"] not in chosen_ids]
    quiz_statuses = set(config.get("quiz_statuses") or ["complete"])
    quizzes = quizzes_by_id(events_with_folders, quiz_statuses, report)
    log("events: " + str(len(events_with_folders)) + ", quizzes to import: " + str(len(quizzes)))

    try:
        topics_by_question = convert.category_index(client.get_json("question/all").get("questions") or [])
    except NotFound:
        topics_by_question = {}
        report.warnings.append("question/all not found: problems have no suggested topic")

    problems = collect_problems(client, quizzes, report)
    competitions_dir = Path(coach_dir) / "competitions"
    for (folder, question_id), entry in sorted(problems.items()):
        problem_dir = competitions_dir / folder / "problems" / str(question_id)
        topics = topics_by_question.get(question_id, [])
        write_problem(client, problem_dir, folder, entry["question"], entry["refs"], topics, report)
        report.problems_per_event[folder] = report.problems_per_event.get(folder, 0) + 1
    return report
