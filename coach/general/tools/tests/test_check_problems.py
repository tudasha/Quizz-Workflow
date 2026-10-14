import check_problems
from fsquiz import convert


def write_problem(coach_dir, folder="fsg", question_id=7, solution=None, **changes):
    fields = {
        "id": question_id,
        "event": folder,
        "year": 2024,
        "rules_year": 2024,
        "quizzes": [{"quiz_id": 1, "year": 2024, "class": "ev", "position": 3}],
        "type": "input",
        "time_s": 120,
        "topic": ["electronics"],
        "options": [],
        "answer": "6.48",
        "unit": "kWh",
        "rule_refs": [],
        "source": "https://fs-quiz.eu/question/7",
        "status": "unverified",
        "verified_by": None,
    }
    fields.update(changes)
    problem_dir = coach_dir / "competitions" / folder / "problems" / str(question_id)
    problem_dir.mkdir(parents=True)
    (problem_dir / "problem.md").write_text(convert.render_problem(fields, "# Problem\n\nText\n"), encoding="utf-8")
    if solution is not None:
        (problem_dir / "solution.py").write_text(solution, encoding="utf-8")
    return problem_dir


def errors_for(problem_dir):
    return check_problems.check_problem(problem_dir, check_problems.load_validator())


def test_a_correct_problem_and_solution_pass(tmp_path):
    problem_dir = write_problem(tmp_path, solution="print('working...')\nprint('6.480')\n")
    assert errors_for(problem_dir) == []


def test_a_wrong_solution_fails(tmp_path):
    problem_dir = write_problem(tmp_path, solution="print(6.47)\n")
    assert errors_for(problem_dir) == ["solution.py printed '6.47' but the answer is '6.48'"]


def test_a_crashing_solution_fails(tmp_path):
    problem_dir = write_problem(tmp_path, solution="raise ValueError('bad input')\n")
    assert errors_for(problem_dir) == ["solution.py failed: ValueError: bad input"]


def test_labels_are_checked_against_the_schema_and_folders(tmp_path):
    assert errors_for(write_problem(tmp_path, question_id=1, topic=["astrology"]))
    assert errors_for(write_problem(tmp_path, question_id=2, status="verified"))
    assert errors_for(write_problem(tmp_path, question_id=3, event="fsa")) == ["event is 'fsa' but the folder is 'fsg'"]
    choice_errors = errors_for(write_problem(tmp_path, question_id=4, type="single-choice", options=["A", "B"], answer="C"))
    assert choice_errors == ["answer not among the options: C"]


def test_verified_problem_needs_a_checker_and_an_answer(tmp_path):
    assert errors_for(write_problem(tmp_path, question_id=1, status="verified", verified_by="Gion")) == []
    assert errors_for(write_problem(tmp_path, question_id=2, status="verified", verified_by="Gion", answer=None))


def test_missing_image_is_reported(tmp_path):
    problem_dir = write_problem(tmp_path)
    (problem_dir / "problem.md").write_text(
        (problem_dir / "problem.md").read_text(encoding="utf-8") + "\n![](images/gone.png)\n", encoding="utf-8"
    )
    assert errors_for(problem_dir) == ["problem.md links a missing image: images/gone.png"]


def test_main_returns_1_when_any_problem_fails(tmp_path, capsys):
    write_problem(tmp_path, question_id=1)
    write_problem(tmp_path, question_id=2, solution="print(1)\n")
    assert check_problems.main(["--coach-dir", str(tmp_path)]) == 1
    assert "checked 2 problems, 1 with errors" in capsys.readouterr().out
    assert check_problems.main(["--coach-dir", str(tmp_path), "--skip-solutions"]) == 0
