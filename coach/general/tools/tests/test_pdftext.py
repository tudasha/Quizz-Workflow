import collections

from fsquiz import pdftext


def counts(text):
    return collections.Counter(text.split())


def test_clean_line_spaces_rule_numbers_and_drops_ligatures():
    assert pdftext.clean_line("see EV4.6 and D1.1.10 \ufb01rst") == "see EV 4.6 and D 1.1.10 first"
    assert pdftext.clean_line("D9 Dynamic Disciplines Scoring") == "D 9 Dynamic Disciplines Scoring"
    assert pdftext.clean_line("AT\u200b 1.1   Formula   Student") == "AT 1.1 Formula Student"
    assert pdftext.clean_line("AT 1\u200bAdministrative Regulations") == "AT 1 Administrative Regulations"
    assert pdftext.clean_line("DV _SCORE = Pmax") == "DV_SCORE = Pmax"


def test_clean_line_mends_plain_extraction_glitches():
    assert pdftext.clean_line("DOO 2 s 0 .2 s, seeT 6.2 and inIN 7, within30 s") == "DOO 2 s 0.2 s, see T 6.2 and in IN 7, within 30 s"


def test_clean_line_leaves_other_numbers_alone():
    assert pdftext.clean_line("M8.8 bolt, 600 V CAT III, 10 mA, 1. 5 cones") == "M8.8 bolt, 600 V CAT III, 10 mA, 1. 5 cones"
    assert pdftext.clean_line("the crazy20 winner") == "the crazy20 winner"


def test_merge_page_joins_small_caps_split_by_plain_extraction():
    layout = "D 9 DYNAMIC DISCIPLINES SCORING\nLow Voltage System\nGREEN FLAG"
    plain = "D 9 D YNAMIC DISCIPLINES SCORING\nLow V oltage System\nG REEN FLAG"
    assert pdftext.merge_page(plain, layout, counts(layout)) == layout


def test_merge_page_keeps_real_words_and_numbers_apart():
    layout = "A TSAL is fitted. Put it into the box. go in to the pit EV4.7.34 mm jacks (a)Conduction"
    plain = "A TSAL is fitted. go in to the pit\nEV 4.7.3 4 mm jacks\n(a) Conduction"
    assert pdftext.merge_page(plain, layout, counts(layout)) == plain


def test_merge_page_uses_layout_when_plain_has_one_word_per_line():
    plain = "Medical\n \nCentre\n \nIn\n \nthe\n \nevent"
    layout = "Medical    Centre  In the event"
    assert pdftext.merge_page(plain, layout, counts(layout)) == layout


def test_merge_pages_takes_words_from_every_page():
    plain_pages = ["receiving a G REEN FLAG", "a GREEN FLAG, then another GREEN FLAG"]
    layout_pages = ["receiving a G  REEN FLAG", "a GREEN FLAG, then another GREEN FLAG"]
    assert pdftext.merge_pages(plain_pages, layout_pages)[0] == "receiving a GREEN FLAG"


def test_clean_pages_drops_footers_and_running_section_headers():
    pages = [
        "D 8.3.5 Each lap is timed\nD 9 DYNAMIC DISCIPLINES SCORING\nD 9.1.1 Points are given\nRules 2026 Version: 1.1 1 of 3",
        "D 9 Dynamic Disciplines Scoring\nTable 11: Tmax\nRules 2026 Version: 1.1 2 of 3",
        "D 10 PENALTIES\nD 10.1.1 Cones\nRules 2026 Version: 1.1 3 of 3",
    ]
    assert pdftext.clean_pages(pages) == [
        "D 8.3.5 Each lap is timed\nD 9 DYNAMIC DISCIPLINES SCORING\nD 9.1.1 Points are given",
        "Table 11: Tmax",
        "D 10 PENALTIES\nD 10.1.1 Cones",
    ]


def test_clean_pages_keeps_numbers_inside_a_page():
    pages = ["1\nSpeed\n5\nkm/h\nFooter", "2\nMass\n200\nkg\nFooter", "3\nPower\n80\nkW\nFooter"]
    assert pdftext.clean_pages(pages) == ["Speed\n5\nkm/h", "Mass\n200\nkg", "Power\n80\nkW"]


def test_changelog_rows_join_wrapped_changes():
    page = "CHANGELOG\nRule Version Change\nA 1.2.4 1.0 Updated wording to use\n“discipline”\nDE 1.0 Renamed to “Event Handbook”\nD 9.1.1 1.1 Adapted Tmax"
    assert pdftext.changelog_rows(["Contents", page]) == [
        ("A 1.2.4", "1.0", "Updated wording to use “discipline”"),
        ("DE", "1.0", "Renamed to “Event Handbook”"),
        ("D 9.1.1", "1.1", "Adapted Tmax"),
    ]


def test_changes_markdown_is_a_table():
    markdown = pdftext.changes_markdown("FS-Rules_2026_v1.1", [("D 9.1.1", "1.0", "a | b")])
    assert "| D 9.1.1 | 1.0 | a \\| b |" in markdown
    assert markdown.startswith("# Changes in FS-Rules_2026_v1.1\n")


def test_heading_number_comes_from_the_page():
    page = "A 1 COMPETITION OVERVIEW\nA 1.1 Competition Objective\nA 1.1.1 Teams"
    assert pdftext.heading_number("Competition Objective", page) == "A 1.1"
    assert pdftext.heading_number("Competition Overview", page) == "A 1"
    assert pdftext.heading_number("AT 1.1 Formula Student Austria", page) == ""
    assert pdftext.heading_number("Not on this page", page) == ""


def test_index_markdown_nests_headings_with_pages():
    pages = ["A ADMINISTRATIVE REGULATIONS\nA 1 COMPETITION OVERVIEW\nA 1.1 Competition Objective"]
    entries = [(0, "Administrative Regulations", 1), (1, "Competition Overview", 1), (2, "Competition Objective", 1)]
    markdown = pdftext.index_markdown("FS-Rules", entries, pages)
    assert markdown.endswith(
        "- A Administrative Regulations, p. 1\n  - A 1 Competition Overview, p. 1\n    - A 1.1 Competition Objective, p. 1\n"
    )


def test_index_markdown_shortens_bookmarks_that_carry_rule_text():
    title = "AT 1.8.2 Number of Drivers (Change of Rules 2026/D 1.2.1)In total, a minimum of four and a maximum of six drivers"
    markdown = pdftext.index_markdown("FSA", [(0, title, 4)], [""])
    assert "- AT 1.8.2 Number of Drivers (Change of Rules 2026/D 1.2.1)In total, a minimum of four and ..., p. 4" in markdown
