from fake_api import CONFIG, FakeClient, files, routes

from fsquiz import convert
from fsquiz.importer import import_problems


def run_import(coach_dir, config=CONFIG, api_routes=None):
    client = FakeClient(api_routes or routes(), files())
    return import_problems(client, coach_dir, config, log=lambda message: None), client


def read_problem(coach_dir, folder, question_id):
    text = (coach_dir / "competitions" / folder / "problems" / str(question_id) / "problem.md").read_text(encoding="utf-8")
    return convert.parse_front_matter(text)


def test_import_writes_each_problem_in_every_event_of_the_quiz(tmp_path):
    report, _ = run_import(tmp_path)
    for folder in ("fs-netherlands", "fs-switzerland"):
        fields, body = read_problem(tmp_path, folder, 1)
        assert fields["event"] == folder
        assert fields["answer"] == "135 GPa"
        assert fields["options"] == ["135 GPa", "180 GPa"]
        assert fields["topic"] == ["math", "mechanics"]
        assert fields["quizzes"] == [{"quiz_id": 1, "year": 2019, "class": "ev", "position": 1}]
        assert "Young's Modulus" in body and "![](images/12_1.jpg)" in body
    assert report.problems_written == 4
    assert report.problems_per_event == {"fs-netherlands": 2, "fs-switzerland": 2}
    # Quiz 7 is unpublished, so only the shared quiz 1 is imported.
    assert report.quizzes_imported == 1 and report.quizzes_skipped == 1


def test_import_downloads_question_solution_and_inline_images(tmp_path):
    run_import(tmp_path)
    problem_dir = tmp_path / "competitions" / "fs-netherlands" / "problems"
    assert (problem_dir / "1" / "images" / "12_1.jpg").read_bytes() == b"jpg"
    assert (problem_dir / "1" / "images" / "s_1.png").read_bytes() == b"png"
    assert (problem_dir / "2" / "images" / "abc.jpg").read_bytes() == b"inline"
    fields, body = read_problem(tmp_path, "fs-netherlands", 2)
    assert fields["type"] == "input" and fields["answer"] == "6.48" and fields["time_s"] == 300
    assert "1 < x?" in body and "![](images/abc.jpg)" in body
    assert (problem_dir / "1" / "solution.md").read_text(encoding="utf-8").startswith(convert.IMPORTED_MARKER)
    assert not (problem_dir / "2" / "solution.md").exists()


def test_second_run_changes_nothing(tmp_path):
    run_import(tmp_path)
    report, client = run_import(tmp_path)
    assert report.problems_written == 0 and report.problems_unchanged == 4
    assert report.solutions_written == 0
    assert client.downloaded == []


def test_verified_and_hand_edited_files_are_left_alone(tmp_path):
    run_import(tmp_path)
    problem_dir = tmp_path / "competitions" / "fs-netherlands" / "problems" / "1"
    verified = convert.render_problem(
        dict(read_problem(tmp_path, "fs-netherlands", 1)[0], status="verified", verified_by="Gion", answer="136 GPa"), "# mine\n"
    )
    (problem_dir / "problem.md").write_text(verified, encoding="utf-8")
    (problem_dir / "solution.md").write_text("# My own solution\n", encoding="utf-8")
    report, _ = run_import(tmp_path)
    assert (problem_dir / "problem.md").read_text(encoding="utf-8") == verified
    assert (problem_dir / "solution.md").read_text(encoding="utf-8") == "# My own solution\n"
    assert report.problems_protected == 1


def test_topic_checker_edits_survive_a_reimport(tmp_path):
    run_import(tmp_path)
    fields, body = read_problem(tmp_path, "fs-netherlands", 2)
    fields.update(topic=["electronics"], unit="kWh", rule_refs=["EV 4.1"])
    problem_file = tmp_path / "competitions" / "fs-netherlands" / "problems" / "2" / "problem.md"
    problem_file.write_text(convert.render_front_matter(fields) + body, encoding="utf-8")
    run_import(tmp_path)
    fields, _ = read_problem(tmp_path, "fs-netherlands", 2)
    assert fields["topic"] == ["electronics"] and fields["unit"] == "kWh" and fields["rule_refs"] == ["EV 4.1"]


def test_event_filter_by_short_name_and_folder_names(tmp_path):
    config = dict(CONFIG, events=["Fsch"], folder_names={"FSCH": "fsch"})
    report, _ = run_import(tmp_path, config)
    assert report.problems_per_event == {"fsch": 2}
    assert not (tmp_path / "competitions" / "fs-netherlands").exists()
    assert report.events_imported == ["FSCH (Formula Student Switzerland) -> fsch"]
    assert report.events_left_out == ["FSN (Formula Student Netherlands)"]


def test_event_filter_by_part_of_the_name(tmp_path):
    report, _ = run_import(tmp_path, dict(CONFIG, events=["netherlands"]))
    assert report.problems_per_event == {"fs-netherlands": 2}
    report, _ = run_import(tmp_path, dict(CONFIG, skip_events=["Netherlands"]))
    assert list(report.problems_per_event) == ["fs-switzerland"]


def test_image_that_fails_to_download_stays_linked_to_fs_quiz(tmp_path):
    api_routes = routes()
    api_routes["quiz/1"]["questions"][0]["images"].append({"img_id": 2, "path": "gone.jpg"})
    api_routes["quiz/1"]["questions"][0]["solution"][0]["images"].append({"img_id": 3, "path": "solutions/535_1.jpg"})
    report, _ = run_import(tmp_path, api_routes=api_routes)
    assert any("gone.jpg" in warning for warning in report.warnings)
    assert report.problems_written == 4
    _, body = read_problem(tmp_path, "fs-netherlands", 1)
    assert "![](https://img.fs-quiz.eu/gone.jpg)" in body and "![](images/12_1.jpg)" in body
    solution = (tmp_path / "competitions" / "fs-netherlands" / "problems" / "1" / "solution.md").read_text(encoding="utf-8")
    assert "![](https://img.fs-quiz.eu/solutions/535_1.jpg)" in solution
