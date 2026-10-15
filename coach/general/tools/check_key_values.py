"""CI check for coach/general/rules/KEY-VALUES-<year>.md.

Usage (from coach/general/tools): python check_key_values.py [--coach-dir DIR] [--config FILE]
Every "quote" in the file must still be in this year's FS Rules, so a new rules version
or a new year shows which values to update. Exits with 1 on any problem.
"""

import argparse
import json
import re
import sys
from pathlib import Path

from fsquiz import pdftext

TOOLS_DIR = Path(__file__).resolve().parent
_QUOTE = re.compile(r'"([^"]+)"')


def comparable(text):
    """Text as the converter would clean it, without whitespace: a quote may span lines."""
    cleaned = "\n".join(pdftext.clean_line(line) for line in text.splitlines())
    return re.sub(r"\s+", "", cleaned).lower()


def rules_text(rules_dir):
    """The converted rules in current/, without the index and changes files."""
    files = sorted(path for path in (rules_dir / "current").glob("*.md") if not path.name.endswith((".index.md", ".changes.md")))
    return comparable("\n".join(path.read_text(encoding="utf-8") for path in files))


def quotes(markdown):
    return [quote for line in markdown.splitlines() if line.lstrip().startswith("- ") for quote in _QUOTE.findall(line)]


def problems(coach_dir, current_year):
    rules_dir = Path(coach_dir) / "general" / "rules"
    expected = rules_dir / ("KEY-VALUES-" + str(current_year) + ".md")
    found = []
    for path in sorted(rules_dir.glob("KEY-VALUES-*.md")):
        if path != expected:
            found.append(path.name + ": not this year's file; update it for " + str(current_year) + " and rename it")
    if not expected.exists():
        return found + [expected.name + " is missing"]
    text = rules_text(rules_dir)
    for quote in quotes(expected.read_text(encoding="utf-8")):
        if comparable(quote) not in text:
            found.append(expected.name + ": quote not in the current rules: \"" + quote + "\"")
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coach-dir", type=Path, default=TOOLS_DIR.parent.parent)
    parser.add_argument("--config", type=Path, default=TOOLS_DIR / "config.json")
    args = parser.parse_args(argv)

    config = json.loads(args.config.read_text(encoding="utf-8"))
    found = problems(args.coach_dir, config["current_year"])
    for problem in found:
        print(problem)
    print("key values: " + ("ok" if not found else str(len(found)) + " problems"))
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
