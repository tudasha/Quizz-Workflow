"""Command line: python -m fsquiz problems|documents|all|convert (run from coach/general/tools).

`convert` needs no API: it converts the rules and handbooks already in current/ again
from their PDFs (the outdated ones, or all with --force).
"""

import argparse
import json
import sys
from pathlib import Path

from .client import FsQuizClient
from .docs import reconvert_local, sync_documents
from .importer import import_problems

TOOLS_DIR = Path(__file__).resolve().parent.parent
DEFAULT_COACH_DIR = TOOLS_DIR.parent.parent
DEFAULT_CONFIG = TOOLS_DIR / "config.json"
DEFAULT_CACHE_DIR = TOOLS_DIR / ".cache" / "fsquiz"


def problems_summary(report):
    lines = [
        "### Problems",
        "- Competitions: " + ("; ".join(report.events_imported) or "none"),
        "- Other FS Quiz events, not imported: " + ("; ".join(report.events_left_out) or "none"),
        "- Quizzes imported: " + str(report.quizzes_imported) + " (skipped by status: " + str(report.quizzes_skipped) + ")",
        "- Problem files written: " + str(report.problems_written) + ", unchanged: " + str(report.problems_unchanged)
        + ", verified or locked (left alone): " + str(report.problems_protected),
        "- Solutions written: " + str(report.solutions_written) + ", images downloaded: " + str(report.images_downloaded),
        "- Per competition: " + ", ".join(folder + " " + str(count) for folder, count in sorted(report.problems_per_event.items())),
    ]
    return lines + warning_lines(report.warnings)


def documents_summary(report):
    lines = ["### Rules and handbooks"]
    lines += ["- Added: " + path for path in report.added] or ["- Nothing new"]
    lines += ["- Moved to its year folder: " + path for path in report.archived]
    lines += ["- Converted again from the PDF: " + path for path in report.reconverted]
    return lines + warning_lines(report.warnings)


def warning_lines(warnings):
    if not warnings:
        return []
    shown = warnings[:30]
    lines = ["- Warnings (" + str(len(warnings)) + "):"] + ["  - " + warning for warning in shown]
    if len(warnings) > len(shown):
        lines.append("  - ...")
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m fsquiz", description=__doc__)
    parser.add_argument("what", choices=["problems", "documents", "all", "convert"])
    parser.add_argument("--coach-dir", type=Path, default=DEFAULT_COACH_DIR)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--no-cache", action="store_true", help="always ask the API, ignore cached answers")
    parser.add_argument("--summary", type=Path, help="also write the summary to this Markdown file")
    parser.add_argument("--force", action="store_true", help="convert: every document, not only outdated ones")
    args = parser.parse_args(argv)

    if args.what == "convert":
        text = "\n".join(documents_summary(reconvert_local(args.coach_dir, force=args.force))) + "\n"
        print(text)
        return 0
    config = json.loads(args.config.read_text(encoding="utf-8"))
    client = FsQuizClient(cache_dir=None if args.no_cache else DEFAULT_CACHE_DIR)
    summary = []
    if args.what in ("problems", "all"):
        summary += problems_summary(import_problems(client, args.coach_dir, config))
    if args.what in ("documents", "all"):
        summary += documents_summary(sync_documents(client, args.coach_dir, config))
    text = "\n".join(summary) + "\n"
    print(text)
    if args.summary:
        args.summary.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
