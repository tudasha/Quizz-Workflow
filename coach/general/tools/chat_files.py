"""Markdown files for web chats that can't open a zip (A5.5).

Gemini and other web chats read uploaded .md files but not zips, folders, PDFs or images.
For each competition one chat file holds the instructions, the skills, COMPETITION.md and
the key values; the rules, the handbook and the past problems come as separate files, so
a member uploads only what the chat's limit allows. Each coach file becomes a section
headed "File: <path>", so the paths the instructions name can still be found.
"""

import re
from pathlib import Path

PREFIX = "fs-quiz-coach-"
# The skills AGENTS.md always loads, plus quiz-maker. Third-party skills stay in the zip:
# their licences ask for the notice to travel with them and they need a terminal.
CHAT_SKILLS = ("solving-rules", "log-use", "solve-modes", "quiz-maker")
_HEADING = re.compile(r"^(#{1,6})(?=\s)")
_FENCE = re.compile(r"^\s*(```|~~~)")


def demote_headings(markdown, levels=2):
    """Push headings down so a file's "# Title" sits under its "## File:" section.
    Lines in code blocks are left alone: "# comment" there is not a heading."""
    lines = []
    in_code = False
    for line in markdown.splitlines():
        if _FENCE.match(line):
            in_code = not in_code
        elif not in_code:
            line = _HEADING.sub(lambda match: "#" * min(6, len(match.group(1)) + levels), line)
        lines.append(line)
    return "\n".join(lines)


def front_matter_as_code(markdown):
    """YAML front matter in the middle of a file would read as a rule and loose text."""
    if not markdown.startswith("---\n"):
        return markdown
    end = markdown.find("\n---\n", 4)
    if end == -1:
        return markdown
    return "```yaml\n" + markdown[4:end] + "\n```\n" + markdown[end + 5:]


def file_section(coach_dir, relative_path):
    relative_path = Path(relative_path)
    text = (Path(coach_dir) / relative_path).read_text(encoding="utf-8").strip()
    if relative_path.suffix == ".py":
        body = "```python\n" + text + "\n```"
    else:
        body = demote_headings(front_matter_as_code(text))
    return "## File: `" + relative_path.as_posix() + "`\n\n" + body + "\n"


def bundle(title, intro_lines, coach_dir, relative_paths):
    parts = ["# " + title, "", *intro_lines, ""]
    parts += [file_section(coach_dir, path) for path in relative_paths]
    return "\n".join(parts).rstrip() + "\n"


def _markdown_files(folder, coach_dir):
    """Sorted .md files of a folder, the index and changes files before the document."""
    if not folder.exists():
        return []
    files = sorted((path for path in folder.glob("*.md") if path.is_file()), key=lambda path: _document_order(path.name))
    return [path.relative_to(coach_dir) for path in files]


def _document_order(name):
    for order, suffix in ((0, ".index.md"), (1, ".changes.md")):
        if name.endswith(suffix):
            return (name[: -len(suffix)], order)
    return (name[: -len(".md")], 2)


def rules_paths(coach_dir):
    coach_dir = Path(coach_dir)
    return _markdown_files(coach_dir / "general" / "rules" / "current", coach_dir)


def handbook_paths(coach_dir, event):
    coach_dir = Path(coach_dir)
    return _markdown_files(coach_dir / "competitions" / event / "handbook" / "current", coach_dir)


def _problem_order(folder):
    # Newer FS Quiz questions have higher ids; put them first.
    return (0, -int(folder.name)) if folder.name.isdigit() else (1, folder.name)


def problem_paths(coach_dir, event):
    coach_dir = Path(coach_dir)
    problems_dir = coach_dir / "competitions" / event / "problems"
    if not problems_dir.exists():
        return []
    paths = []
    for folder in sorted((path for path in problems_dir.iterdir() if path.is_dir()), key=_problem_order):
        for name in ("problem.md", "solution.md", "solution.py"):
            if (folder / name).is_file():
                paths.append((folder / name).relative_to(coach_dir))
    return paths


def chat_paths(coach_dir, event, year):
    coach_dir = Path(coach_dir)
    candidates = [Path("AGENTS.md"), Path("LOG.md")]
    candidates += [Path("general/skills") / skill / "SKILL.md" for skill in CHAT_SKILLS]
    candidates.append(Path("competitions") / event / "COMPETITION.md")
    skills_dir = coach_dir / "competitions" / event / "skills"
    if skills_dir.exists():
        candidates += sorted(path.relative_to(coach_dir) for path in skills_dir.rglob("*.md"))
    candidates.append(Path("general/rules") / ("KEY-VALUES-" + str(year) + ".md"))
    return [path for path in candidates if (coach_dir / path).is_file()]


def file_names(event, year):
    return {
        "chat": PREFIX + event + "-chat.md",
        "rules": PREFIX + "rules-" + str(year) + ".md",
        "handbook": PREFIX + event + "-handbook-" + str(year) + ".md",
        "problems": PREFIX + event + "-problems.md",
    }


def chat_intro(event, year, version_line, has_handbook, has_problems):
    names = file_names(event, year)
    uploads = ["- `" + names["rules"] + "`: FS Rules " + str(year) + ", with its index and this year's changes"]
    if has_handbook:
        uploads.append("- `" + names["handbook"] + "`: the " + event + " handbook, with its index")
    if has_problems:
        uploads.append("- `" + names["problems"] + "` (if the chat's limit allows): past " + event + " problems with the FS Quiz answers")
    return [
        version_line,
        "",
        "The FS Quiz coach for **" + event + "** in a web chat that can't open the zip. Upload this file and:",
        *uploads,
        "",
        "How to use it:",
        "- This file holds the coach's instructions (`AGENTS.md`), its skills, `COMPETITION.md` and the key values, each under a heading \"File: <path>\". "
        "When a file names a path, find that heading here or in the other uploaded files: `general/rules/current/` is the rules file, "
        "`competitions/" + event + "/handbook/current/` the handbook file, `competitions/" + event + "/problems/` the problems file.",
        "- Only " + event + " is here: work as if the member picked it.",
        "- Not here: PDFs, figures, other competitions and the third-party skills (sympy, uncertainty-and-units, markitdown, "
        "verification-before-completion, dispatching-parallel-agents). Work without them; ask the member for a figure or a PDF page when a question needs one.",
        "- No coach MCP server in this chat: follow \"Without MCP\" in `general/skills/log-use/SKILL.md`.",
        "- Run every calculation in the chat's Python tool. If the chat has none, say so before the answer: the answer was not checked by a script.",
    ]


def document_intro(version_line, what):
    return [version_line, "", what + " Each coach file is a section headed \"File: <path>\"; the paths are the ones `AGENTS.md` names."]


def chat_documents(coach_dir, event, year, version_label):
    """{file name: Markdown} for one competition; the shared rules file included."""
    coach_dir = Path(coach_dir)
    names = file_names(event, year)
    version_line = "Version " + version_label + ", rules and handbooks " + str(year) + "."
    handbooks = handbook_paths(coach_dir, event)
    problems = problem_paths(coach_dir, event)
    documents = {
        names["chat"]: bundle(
            "FS Quiz coach: " + event + " (web chat)",
            chat_intro(event, year, version_line, bool(handbooks), bool(problems)),
            coach_dir,
            chat_paths(coach_dir, event, year),
        ),
        names["rules"]: bundle(
            "FS Rules " + str(year) + " (FS Quiz coach, web chat)",
            document_intro(version_line, "The rules converted from the PDF; formulas and tables may be garbled, check those in `KEY-VALUES-" + str(year) + ".md`."),
            coach_dir,
            rules_paths(coach_dir),
        ),
    }
    if handbooks:
        documents[names["handbook"]] = bundle(
            event + " handbook " + str(year) + " (FS Quiz coach, web chat)",
            document_intro(version_line, "The handbook converted from the PDF; it wins over FS Rules."),
            coach_dir,
            handbooks,
        )
    if problems:
        documents[names["problems"]] = bundle(
            event + " past problems (FS Quiz coach, web chat)",
            document_intro(version_line, "Newest first. Figures are not included: a problem that has one links to `images/`, ask the member for it."),
            coach_dir,
            problems,
        )
    return documents


def write_chat_files(coach_dir, out_dir, events, year, version_label):
    """Write every competition's chat files. Returns {file name: size in bytes}."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    sizes = {}
    for event in events:
        for name, markdown in chat_documents(coach_dir, event, year, version_label).items():
            path = out_dir / name
            path.write_text(markdown, encoding="utf-8")
            sizes[name] = path.stat().st_size
    return sizes
