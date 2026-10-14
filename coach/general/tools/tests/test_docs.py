import json

from fake_api import CONFIG, FSCH, FSN, FakeClient, event_all

from fsquiz import docs


def document(doc_id, doc_type, path, version, events, year=2026):
    return {"doc_id": doc_id, "type": doc_type, "path": path, "year": year, "version": version, "event": events}


def fake_page_texts(pdf_path):
    return ["Page one of " + pdf_path.name, "T 11.2 Main hoop"]


def make_client(documents_by_type, year=2026):
    api_routes = {"event/all": event_all()}
    for doc_type, documents in documents_by_type.items():
        api_routes["document?start_id=1&type=" + doc_type + "&year=" + str(year)] = {"documents": documents}
    pdf_files = {}
    for documents in documents_by_type.values():
        for item in documents:
            pdf_files["https://doc.fs-quiz.eu/" + item["path"]] = b"%PDF-1.4 fake"
    return FakeClient(api_routes, pdf_files)


def run_sync(coach_dir, client, config=CONFIG):
    return docs.sync_documents(client, coach_dir, config, log=lambda message: None, page_texts=fake_page_texts)


def test_series_name_ignores_the_version():
    assert docs.series_name("FSG26_Competition_Handbook_v1.0.pdf") == docs.series_name("FSG26_Competition_Handbook_v1.1.pdf")
    assert docs.series_name("Registration_procedure_rev.3.pdf") == docs.series_name("Registration_procedure_rev.4.pdf")
    assert docs.series_name("FS-Rules_2026_v1.0.pdf") != docs.series_name("FSG26_Competition_Handbook_v1.0.pdf")


def test_version_key_compares_numbers_not_text():
    assert docs.version_key({"version": "1.10", "doc_id": 1}) > docs.version_key({"version": "1.9", "doc_id": 2})


def test_fs_rules_go_to_general_and_handbooks_to_their_competitions():
    rules = document(1, "Rulebook", "FS-Rules_2026_v1.0.pdf", "1.0", [FSN, FSCH])
    event_rules = document(2, "Rulebook", "Formula_Student_Spain_Rules_2026_v1.0.pdf", "1.0", [FSCH])
    handbook = document(3, "Handbook", "FSN26_Handbook_v1.0.pdf", "1.0", [FSN])
    folders = {"FSN": "fsn", "FSCH": "fsch"}
    assert docs.target_folders(rules, CONFIG, folders) == ["general/rules"]
    assert docs.target_folders(event_rules, CONFIG, folders) == ["competitions/fsch/handbook"]
    assert docs.target_folders(handbook, CONFIG, folders) == ["competitions/fsn/handbook"]
    assert docs.target_folders(document(4, "Registration", "r.pdf", "1", [FSN]), CONFIG, folders) == []


def test_wanted_documents_keeps_newest_version_of_the_current_year():
    documents = [
        document(1, "Handbook", "FSN26_Handbook_v1.0.pdf", "1.0", [FSN]),
        document(2, "Handbook", "FSN26_Handbook_v1.1.pdf", "1.1", [FSN]),
        document(3, "Handbook", "FSN25_Handbook_v1.0.pdf", "1.0", [FSN], year=2025),
    ]
    wanted = docs.wanted_documents(documents, CONFIG, {"FSN": "fsn"})
    assert [item["path"] for item in wanted["competitions/fsn/handbook"]] == ["FSN26_Handbook_v1.1.pdf"]


def test_sync_downloads_converts_and_records_documents(tmp_path):
    client = make_client({
        "Rulebook": [document(1, "Rulebook", "FS-Rules_2026_v1.0.pdf", "1.0", [])],
        "Handbook": [document(2, "Handbook", "FSN26_Handbook_v1.0.pdf", "1.0", [FSN])],
    })
    report = run_sync(tmp_path, client)
    rules_dir = tmp_path / "general" / "rules" / "current"
    assert (rules_dir / "FS-Rules_2026_v1.0.pdf").exists()
    markdown = (rules_dir / "FS-Rules_2026_v1.0.md").read_text(encoding="utf-8")
    assert "<!-- page 2 -->" in markdown and "T 11.2 Main hoop" in markdown
    manifest = json.loads((rules_dir / "documents.json").read_text(encoding="utf-8"))
    assert manifest[0]["version"] == "1.0" and manifest[0]["year"] == 2026
    assert (tmp_path / "competitions" / "fs-netherlands" / "handbook" / "current" / "FSN26_Handbook_v1.0.md").exists()
    assert len(report.added) == 2


def test_new_version_moves_the_old_one_to_its_year_folder(tmp_path):
    run_sync(tmp_path, make_client({"Handbook": [document(2, "Handbook", "FSN26_Handbook_v1.0.pdf", "1.0", [FSN])]}))
    newer = make_client({"Handbook": [
        document(2, "Handbook", "FSN26_Handbook_v1.0.pdf", "1.0", [FSN]),
        document(5, "Handbook", "FSN26_Handbook_v1.1.pdf", "1.1", [FSN]),
    ]})
    report = run_sync(tmp_path, newer)
    handbook_dir = tmp_path / "competitions" / "fs-netherlands" / "handbook"
    assert sorted(path.name for path in (handbook_dir / "current").iterdir()) == [
        "FSN26_Handbook_v1.1.md", "FSN26_Handbook_v1.1.pdf", "documents.json",
    ]
    assert (handbook_dir / "2026" / "FSN26_Handbook_v1.0.pdf").exists()
    assert (handbook_dir / "2026" / "FSN26_Handbook_v1.0.md").exists()
    assert len(report.archived) == 1


def test_second_sync_changes_nothing(tmp_path):
    client = make_client({"Rulebook": [document(1, "Rulebook", "FS-Rules_2026_v1.0.pdf", "1.0", [])]})
    run_sync(tmp_path, client)
    report = run_sync(tmp_path, client)
    assert report.added == [] and report.archived == [] and report.unchanged == 1


def test_next_year_archives_the_old_rules(tmp_path):
    run_sync(tmp_path, make_client({"Rulebook": [document(1, "Rulebook", "FS-Rules_2026_v1.0.pdf", "1.0", [])]}))
    next_year = make_client({"Rulebook": [document(9, "Rulebook", "FS-Rules_2027_v1.0.pdf", "1.0", [], year=2027)]}, year=2027)
    run_sync(tmp_path, next_year, dict(CONFIG, current_year=2027))
    rules_dir = tmp_path / "general" / "rules"
    assert (rules_dir / "2026" / "FS-Rules_2026_v1.0.pdf").exists()
    assert (rules_dir / "current" / "FS-Rules_2027_v1.0.md").exists()
    assert not (rules_dir / "current" / "FS-Rules_2026_v1.0.pdf").exists()


def test_pages_to_markdown_has_title_source_and_page_markers():
    markdown = docs.pages_to_markdown("FS-Rules", "https://doc.fs-quiz.eu/x.pdf", ["a ", "b"])
    assert markdown.startswith("# FS-Rules\n\nSource: https://doc.fs-quiz.eu/x.pdf")
    assert markdown.endswith("<!-- page 1 -->\n\na\n\n<!-- page 2 -->\n\nb\n")


def test_pdf_page_texts_reads_every_page(tmp_path):
    from pypdf import PdfWriter

    writer = PdfWriter()
    writer.add_blank_page(width=200, height=200)
    writer.add_blank_page(width=200, height=200)
    pdf_path = tmp_path / "blank.pdf"
    with open(pdf_path, "wb") as pdf_file:
        writer.write(pdf_file)
    assert docs.pdf_page_texts(pdf_path) == ["", ""]
