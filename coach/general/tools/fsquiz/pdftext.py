"""Clean the text read from rulebook and handbook PDFs, and build a heading index and a
list of changes from it.

Only pure functions live here (no PDF reading, no disk), so the cleanup can be tested
with plain strings.
"""

import collections
import re

LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi", "\ufb04": "ffl", "\ufb05": "st", "\ufb06": "st"}
# A zero-width space often separates a heading's number from its title ("AT 1\u200bAdministrative").
INVISIBLE = {**dict.fromkeys(map(ord, "\u200c\u200d\u2060\ufeff\u00ad")), ord("\u200b"): " "}
INDEX_TITLE_LIMIT = 90

# FS Rules chapters. Layout extraction drops the space in "D 9.1.1"; agents search with it.
RULE_PREFIXES = ("CV", "EV", "IN", "A", "T", "S", "D")
_RULE_WITH_DOTS = re.compile(r"\b(" + "|".join(RULE_PREFIXES) + r")(\d+(?:\.\d+)+)\b")
_CHAPTER_HEADING = re.compile(r"^(" + "|".join(RULE_PREFIXES) + r")(\d+) ")
_SPACE_BEFORE_UNDERSCORE = re.compile(r"(\w) _(\w)")
# Plain extraction glitches: "0 .2 s", "seeT 6.2", "within30 s".
_SPLIT_DECIMAL = re.compile(r"(\d) \.(\d)")
_GLUED_RULE = re.compile(r"([a-z]{2,})(" + "|".join(RULE_PREFIXES) + r")(?= ?\d)")
# Only short words that come before numbers in rule text; names like "crazy20" stay whole.
_GLUED_NUMBER = re.compile(r"\b(within|than|least|of|to|two|exceed|between|from|at|by|max|min|above|below|under|over)(\d)")
# Bullets and "(a)", "(ii)" items: layout mode glues them to the next word.
_LIST_MARKER = re.compile(r"^([•▪●○■◦–-]|\(?([a-z]|[ivx]+)\))$")

# Running headers and footers sit in the first or last lines of a page.
EDGE_LINES = 3
REPEATED_SHARE = 0.4
REPEATED_MIN_PAGES = 3

_CHANGELOG_HEADER = re.compile(r"^rule\s+version\s+change$", re.IGNORECASE)
_CHANGELOG_ROW = re.compile(r"^([A-Z]{1,3}(?: \d+(?:\.\d+)*)?)\s+(\d+\.\d+(?:\.\d+)?)\s+(.+)$")
_HEADING_NUMBER = re.compile(r"^([A-Z]{1,3}(?: ?\d+(?:\.\d+)*)?|[IVX]+\.(?:\d+(?:\.\d+)*)?|\d+(?:\.\d+)*\.?)$")


def is_word_per_line(text):
    """Some PDFs come out of plain extraction with one word per line."""
    lines = [line for line in (text or "").splitlines() if line.strip()]
    single_words = sum(1 for line in lines if len(line.split()) <= 1)
    return bool(lines) and single_words > 0.5 * len(lines)


def _fragment_run(tokens, start, word_counts):
    """How many tokens from start form one word of the layout text, 0 if none. Small caps
    and kerning split words in plain text ("D YNAMIC", "V oltage"). A run is joined only
    when a part is rarer than the whole word, so "A TSAL" or "in to" stay apart."""
    for length in (4, 3, 2):
        run = tokens[start:start + length]
        if len(run) < length or any(any(char.isdigit() for char in token) or _LIST_MARKER.match(token) for token in run):
            continue
        whole_count = word_counts["".join(run)]
        if whole_count and any(word_counts[token] < whole_count for token in run):
            return length
    return 0


def merge_page(plain_text, layout_text, word_counts):
    """Text of one PDF page from pypdf's two extraction modes.

    Plain mode keeps the gap between a rule number and its text ("EV 4.7.3 4 mm"); layout
    mode can lose it ("EV4.7.34 mm"), so plain is used and the layout words only help to
    join split ones. Pages that plain mode breaks into one word per line use layout."""
    plain_text = plain_text or ""
    if is_word_per_line(plain_text):
        return layout_text or ""
    lines = []
    for line in plain_text.splitlines():
        tokens = line.split()
        joined = []
        index = 0
        while index < len(tokens):
            length = _fragment_run(tokens, index, word_counts) or 1
            joined.append("".join(tokens[index:index + length]))
            index += length
        lines.append(" ".join(joined))
    return "\n".join(lines)


def merge_pages(plain_pages, layout_pages):
    """merge_page for a whole document; a word layout mode splits on one page ("G REEN
    FLAG") is usually whole on another, so the words are counted over every page."""
    word_counts = collections.Counter()
    for layout_text in layout_pages:
        word_counts.update((layout_text or "").split())
    return [merge_page(plain, layout, word_counts) for plain, layout in zip(plain_pages, layout_pages)]


def clean_line(line):
    for ligature, letters in LIGATURES.items():
        line = line.replace(ligature, letters)
    line = line.translate(INVISIBLE)
    # Layout extraction keeps the column gaps; one space reads and searches better.
    line = re.sub(r"\s+", " ", line).strip()
    line = _SPLIT_DECIMAL.sub(r"\1.\2", line)
    line = _GLUED_RULE.sub(r"\1 \2", line)
    line = _GLUED_NUMBER.sub(r"\1 \2", line)
    line = _RULE_WITH_DOTS.sub(r"\1 \2", line)
    line = _CHAPTER_HEADING.sub(r"\1 \2 ", line)
    return _SPACE_BEFORE_UNDERSCORE.sub(r"\1_\2", line)


def _shape(line):
    """A line with its numbers hidden, so "Version 1.1 2 of 135" matches on every page."""
    return re.sub(r"\d+", "#", line).lower()


def _edge_indexes(lines):
    filled = [index for index, line in enumerate(lines) if line]
    return set(filled[:EDGE_LINES] + filled[-EDGE_LINES:])


def repeated_edge_lines(pages_lines):
    """Shapes of lines that appear at the top or bottom of many pages: headers and footers."""
    counts = collections.Counter()
    for lines in pages_lines:
        counts.update({_shape(lines[index]) for index in _edge_indexes(lines)})
    limit = max(REPEATED_MIN_PAGES, REPEATED_SHARE * len(pages_lines))
    return {shape for shape, count in counts.items() if count >= limit}


def _running_section_headers(pages_lines):
    """First lines of pages that repeat a heading found elsewhere ("D 9 Dynamic Disciplines
    Scoring" above "D 9 DYNAMIC DISCIPLINES SCORING"): the section name printed on each page."""
    other_lines = collections.Counter()
    for lines in pages_lines:
        filled = [line for line in lines if line]
        other_lines.update(line.lower() for line in filled[1:])
    headers = set()
    for page_number, lines in enumerate(pages_lines):
        filled = [line for line in lines if line]
        if filled and other_lines[filled[0].lower()]:
            headers.add(page_number)
    return headers


def clean_pages(page_texts):
    """Clean every page: one space between words, no ligatures, rule numbers as "D 9.1.1",
    and no running headers or footers. Returns one text per page."""
    pages_lines = [[clean_line(line) for line in (text or "").splitlines()] for text in page_texts]
    repeated = repeated_edge_lines(pages_lines)
    with_section_header = _running_section_headers(pages_lines)
    cleaned = []
    for page_number, lines in enumerate(pages_lines):
        edges = _edge_indexes(lines)
        filled = [index for index, line in enumerate(lines) if line]
        first_filled = filled[0] if filled else None
        kept = []
        for index, line in enumerate(lines):
            shape = _shape(line)
            # A bare page number is the first or last line; a bare number further in may be
            # a table value that happens to repeat.
            bare_number = not re.search(r"[a-z]", shape)
            in_zone = index in (filled[0], filled[-1]) if bare_number else index in edges
            if in_zone and shape in repeated:
                continue
            if index == first_filled and page_number in with_section_header:
                continue
            kept.append(line)
        cleaned.append(re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip())
    return cleaned


def changelog_rows(cleaned_pages):
    """(rule, version, change) rows from changelog tables headed "Rule Version Change"."""
    rows = []
    for text in cleaned_pages:
        lines = [line for line in text.splitlines() if line]
        header_index = next((index for index, line in enumerate(lines) if _CHANGELOG_HEADER.match(line)), None)
        if header_index is None:
            continue
        for line in lines[header_index + 1:]:
            match = _CHANGELOG_ROW.match(line)
            if match:
                rows.append([match.group(1), match.group(2), match.group(3)])
            elif rows:
                # A change text that wraps continues the row above.
                rows[-1][2] += " " + line
    return [tuple(row) for row in rows]


def changes_markdown(title, rows):
    lines = [
        "# Changes in " + title,
        "",
        "From the changelog in " + title + ".md. Version 1.0 rows changed from last year's document; "
        "higher versions changed during this year. Read the rule's current text before relying on a change.",
        "",
        "| Rule | Version | Change |",
        "|---|---|---|",
    ]
    lines += ["| " + rule + " | " + version + " | " + change.replace("|", "\\|") + " |" for rule, version, change in rows]
    return "\n".join(lines) + "\n"


def _normalised(text):
    return re.sub(r"\s+", " ", clean_line(text)).strip().lower()


def heading_number(title, page_text):
    """The number printed before a heading on its page ("A 1.1" for "Competition Objective"),
    or "" when the title already has one or the page shows none."""
    wanted = _normalised(title)
    if not wanted or _HEADING_NUMBER.match(wanted.split(" ")[0].upper()):
        return ""
    for line in page_text.splitlines():
        line = _normalised(line)
        if line.endswith(" " + wanted):
            number = line[: -len(wanted)].strip().upper()
            if _HEADING_NUMBER.match(number):
                return number
    return ""


def index_markdown(title, entries, cleaned_pages):
    """A nested list of the PDF's bookmarks with their page. entries: (level, title, page)."""
    lines = [
        "# Index: " + title,
        "",
        "Headings of " + title + ".md with their PDF page, from the PDF's bookmarks. "
        "Search the .md for the number or title to read the rule.",
        "",
    ]
    for level, heading, page in entries:
        heading = clean_line(heading)
        if not heading:
            continue
        if len(heading) > INDEX_TITLE_LIMIT:
            # Some bookmarks carry the rule text after the title.
            heading = heading[:INDEX_TITLE_LIMIT].rsplit(" ", 1)[0] + " ..."
        page_text = cleaned_pages[page - 1] if 0 < page <= len(cleaned_pages) else ""
        number = heading_number(heading, page_text)
        label = (number + " " + heading) if number else heading
        lines.append("  " * level + "- " + label + ", p. " + str(page))
    return "\n".join(lines) + "\n"
