"""Keep the current-year FS Rules and competition handbooks in the coach folder.

Agents rely only on current/ (that is all the zip ships). When a newer version or a
new year replaces a file, the old one moves to <year>/ so old problems can still be
checked against the rules they were answered under.
"""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import convert, pdftext
from .importer import selected_events

MANIFEST_NAME = "documents.json"

# Raise when the PDF-to-Markdown conversion changes: the next import converts the
# documents already in current/ again from their PDFs.
CONVERTER_VERSION = 2

_VERSION_TOKEN = re.compile(r"[ _-]*(v|rev|version)[ ._-]*\d+([._]\d+)*", re.IGNORECASE)


@dataclass
class DocsReport:
    added: list = field(default_factory=list)
    archived: list = field(default_factory=list)
    reconverted: list = field(default_factory=list)
    unchanged: int = 0
    warnings: list = field(default_factory=list)


def version_key(document):
    """Sort key for "1.0", "v1.1", "rev.4": numbers compared as numbers, doc_id breaks ties."""
    numbers = [int(part) for part in re.findall(r"\d+", str(document.get("version") or ""))]
    return numbers, convert.as_int(document.get("doc_id")) or 0


def series_name(path):
    """File name without its version, so v1.0 and v1.1 of one handbook are one series."""
    stem = Path(path).stem
    return _VERSION_TOKEN.sub("", stem).lower()


def is_general_rulebook(document, general_rulebook_pattern):
    if document.get("type") != "Rulebook":
        return False
    return not document.get("event") or re.search(general_rulebook_pattern, document["path"], re.IGNORECASE) is not None


def target_folders(document, config, event_folders):
    """Folders (relative to coach/) whose current/ should hold this document."""
    general_types = config["document_types"]["general"]
    competition_types = config["document_types"]["competition"]
    pattern = config.get("general_rulebook_pattern", r"^FS[-_ ]?Rules")
    if document.get("type") in general_types and is_general_rulebook(document, pattern):
        return ["general/rules"]
    if document.get("type") not in competition_types and document.get("type") != "Rulebook":
        return []
    folders = []
    for event in document.get("event") or []:
        folder = event_folders.get(event.get("short_name"))
        if folder:
            folders.append("competitions/" + folder + "/handbook")
    return folders


def newest_per_series(documents):
    newest = {}
    for document in documents:
        key = (document.get("type"), series_name(document["path"]))
        if key not in newest or version_key(document) > version_key(newest[key]):
            newest[key] = document
    return sorted(newest.values(), key=lambda document: document["path"])


def wanted_documents(documents, config, event_folders):
    """target folder -> newest documents of the current year that belong there."""
    per_folder = {}
    for document in documents:
        if convert.as_int(document.get("year")) != config["current_year"]:
            continue
        for folder in target_folders(document, config, event_folders):
            per_folder.setdefault(folder, []).append(document)
    return {folder: newest_per_series(folder_documents) for folder, folder_documents in per_folder.items()}


def pages_to_markdown(title, source_url, cleaned_pages):
    """Searchable Markdown with a marker per page, so an answer can cite the PDF page."""
    parts = [
        "# " + title,
        "",
        "Source: " + source_url + " (via FS Quiz). Converted from the PDF so agents can search it; "
        "the PDF and the organiser's website are the official text. Formulas and tables may be garbled: "
        "check them in the PDF.",
    ]
    for page_number, page_text in enumerate(cleaned_pages, start=1):
        parts += ["", "<!-- page " + str(page_number) + " -->", "", page_text.strip()]
    return "\n".join(parts).rstrip() + "\n"


def pdf_page_texts(pdf_path):
    from pypdf import PdfReader  # imported here so the rest of the tools work without it

    reader = PdfReader(str(pdf_path))
    plain_pages = [page.extract_text() or "" for page in reader.pages]
    layout_pages = [layout_text(page) for page in reader.pages]
    return pdftext.merge_pages(plain_pages, layout_pages)


def layout_text(page):
    try:
        return page.extract_text(extraction_mode="layout") or ""
    except Exception:  # layout mode fails on some pages (e.g. blank ones); plain text still works
        return ""


def pdf_outline(pdf_path):
    """The PDF's bookmarks as (level, title, page) in reading order; [] when it has none."""
    from pypdf import PdfReader

    entries = []
    try:
        reader = PdfReader(str(pdf_path))
    except Exception:  # no bookmarks is not worth failing the conversion for
        return []

    def walk(items, level):
        for item in items:
            if isinstance(item, list):
                walk(item, level + 1)
                continue
            try:
                page = reader.get_destination_page_number(item) + 1
            except Exception:  # a bookmark without a page is skipped, not fatal
                continue
            entries.append((level, str(item.title), page))

    try:
        walk(reader.outline, 0)
    except Exception:
        return []
    return entries


def write_converted(current_dir, file_name, source_url, page_texts, outline):
    """Write <stem>.md and, when the PDF allows, <stem>.index.md and <stem>.changes.md.
    Returns (markdown name, extra file names)."""
    stem = Path(file_name).stem
    pdf_path = current_dir / file_name
    cleaned_pages = pdftext.clean_pages(page_texts(pdf_path))
    markdown_name = stem + ".md"
    (current_dir / markdown_name).write_text(pages_to_markdown(stem, source_url, cleaned_pages), encoding="utf-8")
    extras = []
    entries = outline(pdf_path)
    if entries:
        extras.append(stem + ".index.md")
        (current_dir / extras[-1]).write_text(pdftext.index_markdown(stem, entries, cleaned_pages), encoding="utf-8")
    rows = pdftext.changelog_rows(cleaned_pages)
    if rows:
        extras.append(stem + ".changes.md")
        (current_dir / extras[-1]).write_text(pdftext.changes_markdown(stem, rows), encoding="utf-8")
    return markdown_name, extras


def read_manifest(current_dir):
    manifest_file = current_dir / MANIFEST_NAME
    if not manifest_file.exists():
        return []
    return json.loads(manifest_file.read_text(encoding="utf-8"))


def write_manifest(current_dir, entries):
    entries = sorted(entries, key=lambda entry: entry["file"])
    (current_dir / MANIFEST_NAME).write_text(json.dumps(entries, indent=4, ensure_ascii=False) + "\n", encoding="utf-8")


def archive_entry(base_dir, current_dir, entry, report):
    archive_dir = base_dir / str(entry["year"])
    archive_dir.mkdir(parents=True, exist_ok=True)
    for file_name in [entry["file"], entry["markdown"]] + entry.get("extras", []):
        source = current_dir / file_name
        if source.exists():
            source.replace(archive_dir / file_name)
    report.archived.append(str(archive_dir / entry["file"]))


def reconvert(current_dir, entry, report, page_texts, outline):
    """Convert a kept document again from its PDF when the converter changed."""
    for file_name in entry.get("extras", []):
        (current_dir / file_name).unlink(missing_ok=True)
    markdown_name, extras = write_converted(current_dir, entry["file"], entry["source"], page_texts, outline)
    report.reconverted.append(str(current_dir / entry["file"]))
    return dict(entry, markdown=markdown_name, extras=extras, converter=CONVERTER_VERSION)


def sync_folder(client, coach_dir, folder, documents, report, page_texts=pdf_page_texts, outline=pdf_outline):
    base_dir = Path(coach_dir) / folder
    current_dir = base_dir / "current"
    current_dir.mkdir(parents=True, exist_ok=True)
    wanted_files = {Path(document["path"]).name: document for document in documents}
    kept_entries = []
    for entry in read_manifest(current_dir):
        if entry["file"] not in wanted_files:
            archive_entry(base_dir, current_dir, entry, report)
        elif entry.get("converter") != CONVERTER_VERSION and (current_dir / entry["file"]).exists():
            kept_entries.append(reconvert(current_dir, entry, report, page_texts, outline))
        else:
            kept_entries.append(entry)
    known_files = {entry["file"] for entry in kept_entries}
    for file_name, document in wanted_files.items():
        if file_name in known_files:
            report.unchanged += 1
            continue
        source_url = convert.document_url(document["path"])
        try:
            client.download(source_url, current_dir / file_name)
            markdown_name, extras = write_converted(current_dir, file_name, source_url, page_texts, outline)
        except Exception as error:  # one broken PDF must not stop the other documents
            report.warnings.append(file_name + ": " + str(error))
            continue
        kept_entries.append({
            "doc_id": convert.as_int(document.get("doc_id")),
            "type": document.get("type"),
            "year": convert.as_int(document.get("year")),
            "version": document.get("version"),
            "file": file_name,
            "markdown": markdown_name,
            "extras": extras,
            "converter": CONVERTER_VERSION,
            "source": source_url,
        })
        report.added.append(str(current_dir / file_name))
    write_manifest(current_dir, kept_entries)


def current_folders(coach_dir):
    """Every current/ folder that holds converted documents."""
    coach_dir = Path(coach_dir)
    folders = [coach_dir / "general" / "rules" / "current"]
    folders += sorted((coach_dir / "competitions").glob("*/handbook/current"))
    return [folder for folder in folders if (folder / MANIFEST_NAME).exists()]


def reconvert_local(coach_dir, force=False, page_texts=pdf_page_texts, outline=pdf_outline):
    """Convert the documents in current/ again from their PDFs, without the API: the ones
    an older converter made, or all of them with force."""
    report = DocsReport()
    for current_dir in current_folders(coach_dir):
        entries = []
        for entry in read_manifest(current_dir):
            outdated = force or entry.get("converter") != CONVERTER_VERSION
            if outdated and (current_dir / entry["file"]).exists():
                entry = reconvert(current_dir, entry, report, page_texts, outline)
            else:
                report.unchanged += 1
            entries.append(entry)
        write_manifest(current_dir, entries)
    return report


def sync_documents(client, coach_dir, config, log=print, page_texts=pdf_page_texts, outline=pdf_outline):
    report = DocsReport()
    events = client.get_json("event/all").get("events") or []
    event_folders = {event["short_name"]: folder for event, folder in selected_events(events, config)}
    document_types = config["document_types"]["general"] + config["document_types"]["competition"]
    documents = []
    for document_type in dict.fromkeys(document_types):
        documents += client.get_all_pages("document", "documents", {"year": config["current_year"], "type": document_type})
    wanted = wanted_documents(documents, config, event_folders)
    log("current-year documents: " + str(sum(len(items) for items in wanted.values())) + " in " + str(len(wanted)) + " folders")
    for folder in sorted(wanted):
        sync_folder(client, coach_dir, folder, wanted[folder], report, page_texts, outline)
    return report
