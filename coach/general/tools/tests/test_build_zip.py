import zipfile
from datetime import datetime, timezone
from pathlib import Path

from fake_api import CONFIG

import build_zip


def make_coach(coach_dir):
    files = [
        "AGENTS.md",
        "LOG.md",
        "general/skills/solving-rules/SKILL.md",
        "general/rules/current/FS-Rules_2026_v1.0.md",
        "general/rules/2025/FS-Rules_2025_v1.0.md",
        "general/tools/build_zip.py",
        "general/tools/.cache/fsquiz/x.json",
        "competitions/README.md",
        "competitions/fsg/COMPETITION.md",
        "competitions/fsg/handbook/current/FSG26_Handbook.md",
        "competitions/fsg/handbook/2025/FSG25_Handbook.md",
        "competitions/fsg/problems/7/problem.md",
        "competitions/fsg/problems/7/__pycache__/solution.cpython-312.pyc",
        "competitions/fsn/problems/1/problem.md",
        "competitions/fsn/problems/1/images/1.jpg.part",
    ]
    for name in files:
        path = coach_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x" * 10, encoding="utf-8")


def as_strings(paths):
    return [Path(path).as_posix() for path in paths]


def test_zip_ships_current_material_only(tmp_path):
    make_coach(tmp_path)
    assert as_strings(build_zip.shipped_files(tmp_path)) == [
        "AGENTS.md",
        "LOG.md",
        "competitions/README.md",
        "competitions/fsg/COMPETITION.md",
        "competitions/fsg/handbook/current/FSG26_Handbook.md",
        "competitions/fsg/problems/7/problem.md",
        "competitions/fsn/problems/1/problem.md",
        "general/rules/current/FS-Rules_2026_v1.0.md",
        "general/skills/solving-rules/SKILL.md",
    ]


def test_one_competition_keeps_general_and_drops_the_others(tmp_path):
    make_coach(tmp_path)
    shipped = as_strings(build_zip.shipped_files(tmp_path, "fsn"))
    assert "competitions/fsn/problems/1/problem.md" in shipped
    assert "general/skills/solving-rules/SKILL.md" in shipped
    assert not any(name.startswith("competitions/fsg/") for name in shipped)


def test_build_writes_zip_with_version_and_root_folder(tmp_path):
    coach_dir = tmp_path / "coach"
    make_coach(coach_dir)
    built_at = datetime(2026, 10, 14, 12, 0, tzinfo=timezone.utc)
    sizes = build_zip.build(coach_dir, tmp_path / "dist", "abc1234", CONFIG, built_at)
    assert list(sizes) == ["fs-quiz-coach.zip"]
    with zipfile.ZipFile(tmp_path / "dist" / "fs-quiz-coach.zip") as archive:
        names = archive.namelist()
        version = archive.read("fs-quiz-coach/VERSION.txt").decode()
    assert "fs-quiz-coach/AGENTS.md" in names
    assert all(name.startswith("fs-quiz-coach/") for name in names)
    assert "Version: abc1234" in version and "Built: 2026-10-14 12:00 UTC" in version
    assert "- fsg: 1 problems" in version and "- fsn: 1 problems" in version


def test_big_zip_is_also_split_per_competition(tmp_path):
    coach_dir = tmp_path / "coach"
    make_coach(coach_dir)
    sizes = build_zip.build(coach_dir, tmp_path / "dist", "x", dict(CONFIG, zip_split_above_mb=0))
    assert sorted(sizes) == ["fs-quiz-coach-fsg.zip", "fs-quiz-coach-fsn.zip", "fs-quiz-coach.zip"]
