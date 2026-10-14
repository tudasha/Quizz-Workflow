"""CI check for coach/competitions/*/problems: labels, images and solution.py answers.

Usage (from coach/general/tools): python check_problems.py [--coach-dir DIR] [--skip-solutions]
Exits with 1 when any problem has an error, so a broken solution.py fails CI.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from fsquiz import convert

TOOLS_DIR = Path(__file__).resolve().parent
SCHEMA_FILE = TOOLS_DIR / "problem.schema.json"
SOLUTION_TIMEOUT_S = 60

_LOCAL_IMAGE = re.compile(r"!\[[^\]]*\]\((images/[^)\s]+)\)")


def load_validator():
    return Draft202012Validator(json.loads(SCHEMA_FILE.read_text(encoding="utf-8")))


def label_errors(fields, problem_dir, validator):
    errors = [error.message for error in validator.iter_errors(fields)]
    if errors:
        return errors
    competition_folder = problem_dir.parent.parent.name
    if fields["event"] != competition_folder:
        errors.append("event is " + repr(fields["event"]) + " but the folder is " + repr(competition_folder))
    if str(fields["id"]) != problem_dir.name:
        errors.append("id is " + str(fields["id"]) + " but the folder is " + repr(problem_dir.name))
    if fields["type"] in convert.CHOICE_TYPES and fields["answer"] is not None:
        answers = fields["answer"] if isinstance(fields["answer"], list) else [fields["answer"]]
        missing = [answer for answer in answers if answer not in fields["options"]]
        if missing:
            errors.append("answer not among the options: " + ", ".join(map(str, missing)))
    return errors


def missing_images(problem_dir):
    errors = []
    for file_name in ("problem.md", "solution.md"):
        markdown_file = problem_dir / file_name
        if not markdown_file.exists():
            continue
        for image_path in _LOCAL_IMAGE.findall(markdown_file.read_text(encoding="utf-8")):
            if not (problem_dir / image_path).exists():
                errors.append(file_name + " links a missing image: " + image_path)
    return errors


def last_printed_line(output):
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    return lines[-1] if lines else None


def run_solution(problem_dir):
    """Run solution.py in its folder. Returns (last printed line, error message)."""
    try:
        result = subprocess.run(
            [sys.executable, "solution.py"],
            cwd=problem_dir,
            capture_output=True,
            text=True,
            timeout=SOLUTION_TIMEOUT_S,
        )
    except subprocess.TimeoutExpired:
        return None, "solution.py ran longer than " + str(SOLUTION_TIMEOUT_S) + " s"
    if result.returncode != 0:
        last_error_line = last_printed_line(result.stderr) or "no error output"
        return None, "solution.py failed: " + last_error_line
    printed = last_printed_line(result.stdout)
    if printed is None:
        return None, "solution.py printed nothing"
    return printed, None


def solution_errors(problem_dir, fields):
    if not (problem_dir / "solution.py").exists():
        return []
    printed, error = run_solution(problem_dir)
    if error:
        return [error]
    if not convert.answers_match(printed, fields.get("answer")):
        return ["solution.py printed " + repr(printed) + " but the answer is " + repr(fields.get("answer"))]
    return []


def check_problem(problem_dir, validator, run_solutions=True):
    problem_file = problem_dir / "problem.md"
    if not problem_file.exists():
        return ["problem.md is missing"]
    try:
        fields, body = convert.parse_front_matter(problem_file.read_text(encoding="utf-8"))
    except Exception as error:  # a YAML error is a finding, not a crash
        return ["front matter does not parse: " + str(error)]
    if not fields:
        return ["problem.md has no front matter"]
    errors = label_errors(fields, problem_dir, validator)
    if not body.strip():
        errors.append("problem.md has no question text")
    errors += missing_images(problem_dir)
    if run_solutions and not errors:
        errors += solution_errors(problem_dir, fields)
    return errors


def problem_dirs(coach_dir):
    return sorted(path for path in Path(coach_dir).glob("competitions/*/problems/*") if path.is_dir())


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coach-dir", type=Path, default=TOOLS_DIR.parent.parent)
    parser.add_argument("--skip-solutions", action="store_true")
    args = parser.parse_args(argv)

    validator = load_validator()
    checked = 0
    failed = 0
    for problem_dir in problem_dirs(args.coach_dir):
        checked += 1
        errors = check_problem(problem_dir, validator, run_solutions=not args.skip_solutions)
        if errors:
            failed += 1
            relative_dir = problem_dir.relative_to(args.coach_dir)
            for error in errors:
                print(str(relative_dir) + ": " + error)
    print("checked " + str(checked) + " problems, " + str(failed) + " with errors")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
