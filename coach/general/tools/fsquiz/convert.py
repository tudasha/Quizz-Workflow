"""Turn FS Quiz API records into the coach's problem files.

Only pure functions live here (no network, no disk), so the format can be tested
without reaching the API.
"""

import html
import json
import re
from decimal import Decimal, InvalidOperation

import yaml

IMAGE_BASE_URL = "https://img.fs-quiz.eu/"
DOCUMENT_BASE_URL = "https://doc.fs-quiz.eu/"
QUESTION_PAGE_URL = "https://fs-quiz.eu/question/{question_id}"

# FS Quiz category flags (from /question/all) mapped to the coach's topic names.
CATEGORY_TOPICS = {
    "math": "math",
    "mechanical": "mechanics",
    "electronic": "electronics",
    "rule": "rules",
    "static": "static-events",
    "dynamic": "dynamic-events",
    "scoring": "scoring",
}

CHOICE_TYPES = ("single-choice", "multi-choice")

# Marker on files the import wrote. A file still carrying it can be refreshed by the
# next import; removing the line tells the import the file is now hand-edited.
IMPORTED_MARKER = (
    "<!-- Imported from FS Quiz. Delete this line to keep your edits when the import runs again. -->"
)

# Front matter keys in the order they are written, so diffs between imports stay small.
FRONT_MATTER_ORDER = (
    "id",
    "event",
    "year",
    "rules_year",
    "quizzes",
    "type",
    "time_s",
    "topic",
    "options",
    "answer",
    "unit",
    "rule_refs",
    "source",
    "status",
    "verified_by",
    "locked",
)

# Once a problem exists, people own these fields: topic checkers fix them by hand and
# the import must not undo that work.
HUMAN_FIELDS = ("topic", "unit", "rule_refs", "rules_year", "status", "verified_by", "locked")

_TAG_PATTERN = re.compile(r"</?(p|div|span|b|i|u|strong|em|font|center)(\s[^>]*)?>", re.IGNORECASE)
_IMG_PATTERN = re.compile(r"<img\b[^>]*?\bsrc\s*=\s*[\"']([^\"']+)[\"'][^>]*>", re.IGNORECASE)
_NUMBER_WITH_REST = re.compile(r"^\s*([-+]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?)\s*(.*?)\s*$")


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")
    return slug or "event"


def event_folder(short_name, folder_overrides=None):
    """Competition folder for an FS Quiz event: its short name in lower case unless
    the config maps it to another name."""
    folder_overrides = folder_overrides or {}
    if short_name in folder_overrides:
        return folder_overrides[short_name]
    return slugify(short_name)


def image_file_name(path):
    """Local file name for an FS Quiz image path ("12_1.jpg", "testquiz/abc.jpg")."""
    base_name = path.replace("\\", "/").rstrip("/").split("/")[-1]
    safe_name = re.sub(r"[^A-Za-z0-9._-]+", "_", base_name)
    return safe_name or "image"


def image_url(path):
    return IMAGE_BASE_URL + path.lstrip("/")


def document_url(path):
    return DOCUMENT_BASE_URL + path.lstrip("/")


def to_markdown(raw_text):
    """Convert FS Quiz HTML-ish text to Markdown.

    Returns (markdown, inline_image_urls). Images hosted on FS Quiz are pointed at
    images/<name> so the zip works offline; the caller downloads them.
    """
    if raw_text is None:
        return "", []
    inline_image_urls = []

    def replace_image(match):
        url = match.group(1).strip()
        if url.startswith(IMAGE_BASE_URL) or url.startswith("http://img.fs-quiz.eu/"):
            inline_image_urls.append(url)
            return "\n\n![](images/" + image_file_name(url) + ")\n\n"
        return "\n\n![](" + url + ")\n\n"

    text = _IMG_PATTERN.sub(replace_image, raw_text)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<sup>(.*?)</sup>", r"^\1", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<sub>(.*?)</sub>", r"_\1", text, flags=re.IGNORECASE | re.DOTALL)
    text = _TAG_PATTERN.sub("", text)
    # Unescape last: an escaped "&lt;" in the source is a real "<" in the question
    # ("x &lt; 5") and must not be taken for a tag above.
    text = html.unescape(text).replace("\r\n", "\n").replace("\xa0", " ")
    lines = [line.rstrip() for line in text.split("\n")]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()
    return text, inline_image_urls


def as_int(value):
    if value is None or value == "":
        return None
    return int(value)


def is_flag_set(value):
    return str(value).strip().lower() in ("1", "true", "yes")


def topics_from_categories(category_row):
    """Topics suggested by FS Quiz's category flags; topic checkers confirm them."""
    if not category_row:
        return []
    return [topic for flag, topic in CATEGORY_TOPICS.items() if is_flag_set(category_row.get(flag))]


def category_index(question_rows):
    """Map question_id -> suggested topics from the /question/all rows."""
    return {as_int(row["question_id"]): topics_from_categories(row) for row in question_rows}


def correct_answers(answers):
    return [answer["answer_text"].strip() for answer in sorted_answers(answers) if answer.get("is_correct")]


def sorted_answers(answers):
    return sorted(answers or [], key=lambda answer: as_int(answer.get("answer_id")) or 0)


def answer_value(answers):
    """One correct answer as a string, several as a list, none as None."""
    correct = correct_answers(answers)
    if not correct:
        return None
    if len(correct) == 1:
        return correct[0]
    return correct


def option_texts(question):
    if question.get("type") not in CHOICE_TYPES:
        return []
    return [answer["answer_text"].strip() for answer in sorted_answers(question.get("answers"))]


def option_label(index):
    return chr(ord("A") + index) if index < 26 else str(index + 1)


def quiz_reference(quiz, position_index):
    return {
        "quiz_id": as_int(quiz["quiz_id"]),
        "year": as_int(quiz["year"]),
        "class": quiz.get("class"),
        "position": as_int(position_index),
    }


def problem_fields(question, event_name, quiz_references, topics, existing_fields=None):
    """Front matter for one problem in one competition folder.

    existing_fields are the fields already on disk: the fields people own are kept,
    everything that comes from FS Quiz is refreshed.
    """
    quiz_references = sorted(quiz_references, key=lambda ref: (ref["year"] or 0, ref["quiz_id"]))
    first_year = quiz_references[0]["year"] if quiz_references else None
    question_id = as_int(question["question_id"])
    fields = {
        "id": question_id,
        "event": event_name,
        "year": first_year,
        # Old problems were answered under their own year's rules (AGENTS.md).
        "rules_year": first_year,
        "quizzes": quiz_references,
        "type": question.get("type"),
        "time_s": as_int(question.get("time")),
        "topic": topics,
        "options": option_texts(question),
        "answer": answer_value(question.get("answers")),
        "unit": None,
        "rule_refs": [],
        "source": QUESTION_PAGE_URL.format(question_id=question_id),
        "status": "unverified",
        "verified_by": None,
    }
    for field_name, value in (existing_fields or {}).items():
        if field_name in HUMAN_FIELDS or field_name not in fields:
            fields[field_name] = value
    return fields


def is_protected(existing_fields):
    """A verified or locked problem belongs to the topic checkers: never rewrite it."""
    if not existing_fields:
        return False
    return existing_fields.get("status") == "verified" or existing_fields.get("locked") is True


def render_front_matter(fields):
    ordered_names = [name for name in FRONT_MATTER_ORDER if name in fields]
    ordered_names += sorted(name for name in fields if name not in FRONT_MATTER_ORDER)
    # JSON is valid YAML and keeps strings with ":" or "#" safe without extra rules.
    lines = [name + ": " + json.dumps(fields[name], ensure_ascii=False) for name in ordered_names]
    return "---\n" + "\n".join(lines) + "\n---\n"


def parse_front_matter(text):
    """Split a Markdown file into (front matter dict, body). No front matter -> ({}, text)."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fields = yaml.safe_load(text[4:end]) or {}
    return fields, text[end + len("\n---\n"):]


def problem_body(question_id, text_markdown, image_names, options):
    parts = ["# Problem " + str(question_id), "", text_markdown]
    for image_name in image_names:
        parts += ["", "![](images/" + image_name + ")"]
    if options:
        parts += ["", "Options:"]
        parts += ["- " + option_label(index) + ") " + option for index, option in enumerate(options)]
    return "\n".join(parts).rstrip() + "\n"


def render_problem(fields, body):
    return render_front_matter(fields) + "\n" + body


def solution_markdown(question_id, solutions):
    """solution.md from FS Quiz's written solutions, or None when there are none.

    Returns (markdown, image_paths, inline_image_urls)."""
    solutions = [solution for solution in (solutions or []) if (solution.get("text") or "").strip() or solution.get("images")]
    if not solutions:
        return None, [], []
    parts = [IMPORTED_MARKER, "# Solution " + str(question_id)]
    image_paths = []
    inline_image_urls = []
    for solution in sorted(solutions, key=lambda item: as_int(item.get("solution_id")) or 0):
        text_markdown, inline_urls = to_markdown(solution.get("text"))
        inline_image_urls += inline_urls
        parts += ["", text_markdown] if text_markdown else []
        for image in solution.get("images") or []:
            image_paths.append(image["path"])
            parts += ["", "![](images/" + image_file_name(image["path"]) + ")"]
    return "\n".join(parts).rstrip() + "\n", image_paths, inline_image_urls


def split_number(text):
    """("135 GPa") -> (Decimal("135"), "gpa"); None when the text does not start with a number."""
    match = _NUMBER_WITH_REST.match(text)
    if not match:
        return None
    number_text = match.group(1)
    if "," in number_text and "." not in number_text:
        number_text = number_text.replace(",", ".")
    try:
        number = Decimal(number_text)
    except InvalidOperation:
        return None
    return number, normalise(match.group(2))


def normalise(text):
    return re.sub(r"\s+", " ", str(text)).strip().lower()


def single_answer_matches(printed, expected):
    printed_number = split_number(printed)
    expected_number = split_number(str(expected))
    if printed_number and expected_number:
        return printed_number == expected_number
    return normalise(printed) == normalise(expected)


def answers_match(printed_line, expected):
    """Does the last line a solution.py printed equal the answer in problem.md?

    Numbers compare by value ("135.0 GPa" == "135 GPa"); several correct options are
    printed on one line separated by ";" in any order.
    """
    if expected is None:
        return False
    if isinstance(expected, list):
        printed_parts = [part for part in printed_line.split(";") if part.strip()]
        if len(printed_parts) != len(expected):
            return False
        remaining = list(expected)
        for part in printed_parts:
            match = next((item for item in remaining if single_answer_matches(part, item)), None)
            if match is None:
                return False
            remaining.remove(match)
        return True
    return single_answer_matches(printed_line, expected)
