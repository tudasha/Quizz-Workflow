"""Build fs-quiz-coach.zip from coach/ (A5.1).

Usage (from coach/general/tools): python build_zip.py --out DIR [--version LABEL]

The zip holds what agents need and nothing else: AGENTS.md, LOG.md, general/ and every
competition folder, with only the current-year rules and handbooks. Import tools and
older rule years stay in the repo. When the zip is bigger than the config limit, one
zip per competition is built too, for agents with a small upload limit (A5.4).
"""

import argparse
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
ZIP_ROOT = "fs-quiz-coach"
ZIP_NAME = ZIP_ROOT + ".zip"

SKIPPED_DIR_NAMES = {"__pycache__", ".pytest_cache", ".cache", ".git", ".venv"}
SKIPPED_SUFFIXES = (".pyc", ".part")
SKIPPED_FILE_NAMES = {".DS_Store", "Thumbs.db"}
_YEAR = re.compile(r"^\d{4}$")


def is_shipped(relative_path):
    """Does this file (path relative to coach/) belong in the zip?"""
    parts = relative_path.parts
    if any(part in SKIPPED_DIR_NAMES for part in parts):
        return False
    if relative_path.name in SKIPPED_FILE_NAMES or relative_path.name.endswith(SKIPPED_SUFFIXES):
        return False
    if parts[:2] == ("general", "tools"):
        return False
    # Older years (rules/2025/, handbook/2025/) are for checking old problems in the repo only.
    if parts[:2] == ("general", "rules") and len(parts) > 3 and _YEAR.match(parts[2]):
        return False
    if parts[0] == "competitions" and len(parts) > 4 and parts[2] == "handbook" and _YEAR.match(parts[3]):
        return False
    return True


def shipped_files(coach_dir, competition=None):
    """Sorted paths (relative to coach/) to put in the zip; one competition only if given."""
    coach_dir = Path(coach_dir)
    files = []
    for path in sorted(coach_dir.rglob("*")):
        if not path.is_file():
            continue
        relative_path = path.relative_to(coach_dir)
        if not is_shipped(relative_path):
            continue
        parts = relative_path.parts
        if competition and parts[0] == "competitions" and len(parts) > 2 and parts[1] != competition:
            continue
        files.append(relative_path)
    return files


def competitions(coach_dir):
    competitions_dir = Path(coach_dir) / "competitions"
    if not competitions_dir.exists():
        return []
    return sorted(path.name for path in competitions_dir.iterdir() if path.is_dir())


def version_text(coach_dir, version_label, current_year, built_at):
    lines = [
        "FS Quiz coach",
        "Version: " + version_label,
        "Built: " + built_at.strftime("%Y-%m-%d %H:%M UTC"),
        "Rules and handbooks: " + str(current_year),
        "Competitions:",
    ]
    for competition in competitions(coach_dir):
        problem_count = len(list((Path(coach_dir) / "competitions" / competition / "problems").glob("*/problem.md")))
        lines.append("- " + competition + ": " + str(problem_count) + " problems")
    return "\n".join(lines) + "\n"


def write_zip(coach_dir, zip_path, files, version):
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        archive.writestr(ZIP_ROOT + "/VERSION.txt", version)
        for relative_path in files:
            archive.write(Path(coach_dir) / relative_path, ZIP_ROOT + "/" + relative_path.as_posix())
    return zip_path.stat().st_size


def build(coach_dir, out_dir, version_label, config, built_at=None):
    """Build the zip(s). Returns {zip file name: size in bytes}."""
    built_at = built_at or datetime.now(timezone.utc)
    out_dir = Path(out_dir)
    version = version_text(coach_dir, version_label, config["current_year"], built_at)
    sizes = {ZIP_NAME: write_zip(coach_dir, out_dir / ZIP_NAME, shipped_files(coach_dir), version)}
    (out_dir / "VERSION.txt").write_text(version, encoding="utf-8")
    if sizes[ZIP_NAME] > config["zip_split_above_mb"] * 1024 * 1024:
        for competition in competitions(coach_dir):
            zip_name = ZIP_ROOT + "-" + competition + ".zip"
            files = shipped_files(coach_dir, competition)
            sizes[zip_name] = write_zip(coach_dir, out_dir / zip_name, files, version)
    return sizes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--coach-dir", type=Path, default=TOOLS_DIR.parent.parent)
    parser.add_argument("--config", type=Path, default=TOOLS_DIR / "config.json")
    parser.add_argument("--out", type=Path, required=True, help="folder for the zip(s)")
    parser.add_argument("--version", default="local", help="label written to VERSION.txt, e.g. the commit")
    args = parser.parse_args(argv)

    config = json.loads(args.config.read_text(encoding="utf-8"))
    for zip_name, size in build(args.coach_dir, args.out, args.version, config).items():
        print(zip_name + ": " + format(size / 1024 / 1024, ".1f") + " MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
