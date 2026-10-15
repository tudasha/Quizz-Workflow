import chat_files

FILES = {
    "AGENTS.md": "# FS Quiz Coach\n\n## 1. Pick the competition\n",
    "LOG.md": "# Connecting the shared log\n",
    "general/skills/solving-rules/SKILL.md": "---\nname: solving-rules\ndescription: How to solve\n---\n\n# Solving rules\n\n```python\n# not a heading\nprint(1)\n```\n",
    "general/skills/log-use/SKILL.md": "# Log use\n",
    "general/skills/sympy/SKILL.md": "# Third-party\n",
    "general/rules/KEY-VALUES-2026.md": "# Key values\n",
    "general/rules/current/FS-Rules_2026_v1.1.md": "# FS-Rules\n",
    "general/rules/current/FS-Rules_2026_v1.1.index.md": "# Index\n",
    "general/rules/current/FS-Rules_2026_v1.1.changes.md": "# Changes\n",
    "competitions/fsg/COMPETITION.md": "# FSG\n",
    "competitions/fsg/handbook/current/FSG26.md": "# FSG handbook\n",
    "competitions/fsg/problems/7/problem.md": "---\nid: 7\n---\n\n# Problem 7\n",
    "competitions/fsg/problems/12/problem.md": "---\nid: 12\n---\n\n# Problem 12\n",
    "competitions/fsg/problems/12/solution.py": "# prints the answer\nprint('4.00')\n",
    "competitions/fsn/COMPETITION.md": "# FSN\n",
}


def make_coach(coach_dir):
    for name, text in FILES.items():
        path = coach_dir / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return coach_dir


def test_demote_headings_skips_code_blocks():
    markdown = "# Title\n## Part\n```python\n# comment\n```\n#hashtag"
    assert chat_files.demote_headings(markdown) == "### Title\n#### Part\n```python\n# comment\n```\n#hashtag"


def test_front_matter_becomes_a_yaml_block():
    assert chat_files.front_matter_as_code("---\nid: 7\n---\n\n# Problem 7") == "```yaml\nid: 7\n```\n\n# Problem 7"
    assert chat_files.front_matter_as_code("# No front matter") == "# No front matter"


def test_chat_file_holds_instructions_skills_competition_and_key_values(tmp_path):
    documents = chat_files.chat_documents(make_coach(tmp_path), "fsg", 2026, "abc1234")
    chat = documents["fs-quiz-coach-fsg-chat.md"]
    sections = [line for line in chat.splitlines() if line.startswith("## File:")]
    assert sections == [
        "## File: `AGENTS.md`",
        "## File: `LOG.md`",
        "## File: `general/skills/solving-rules/SKILL.md`",
        "## File: `general/skills/log-use/SKILL.md`",
        "## File: `competitions/fsg/COMPETITION.md`",
        "## File: `general/rules/KEY-VALUES-2026.md`",
    ]
    assert "### FS Quiz Coach" in chat and "# not a heading" in chat
    assert "fs-quiz-coach-fsg-handbook-2026.md" in chat and "Version abc1234" in chat


def test_rules_handbook_and_problems_files(tmp_path):
    documents = chat_files.chat_documents(make_coach(tmp_path), "fsg", 2026, "x")
    rules_sections = [line for line in documents["fs-quiz-coach-rules-2026.md"].splitlines() if line.startswith("## File:")]
    assert rules_sections == [
        "## File: `general/rules/current/FS-Rules_2026_v1.1.index.md`",
        "## File: `general/rules/current/FS-Rules_2026_v1.1.changes.md`",
        "## File: `general/rules/current/FS-Rules_2026_v1.1.md`",
    ]
    assert "### FSG handbook" in documents["fs-quiz-coach-fsg-handbook-2026.md"]
    problems = documents["fs-quiz-coach-fsg-problems.md"]
    assert problems.index("problems/12/problem.md") < problems.index("problems/12/solution.py") < problems.index("problems/7/problem.md")
    assert "```python\n# prints the answer\nprint('4.00')\n```" in problems


def test_competition_without_handbook_or_problems_gets_no_empty_files(tmp_path):
    documents = chat_files.chat_documents(make_coach(tmp_path), "fsn", 2026, "x")
    assert sorted(documents) == ["fs-quiz-coach-fsn-chat.md", "fs-quiz-coach-rules-2026.md"]
    assert "fsn-handbook" not in documents["fs-quiz-coach-fsn-chat.md"]


def test_write_chat_files_reports_every_file_written(tmp_path):
    coach_dir = make_coach(tmp_path / "coach")
    sizes = chat_files.write_chat_files(coach_dir, tmp_path / "dist", ["fsg", "fsn"], 2026, "x")
    assert sorted(sizes) == sorted(path.name for path in (tmp_path / "dist").iterdir())
    assert "fs-quiz-coach-rules-2026.md" in sizes
