from decimal import Decimal

import pytest

from fsquiz import convert


def test_event_folder_comes_from_the_full_event_name_unless_overridden():
    assert convert.event_folder({"short_name": "FSAA", "event_name": "Formula Student Alpe Adria"}) == "fs-alpe-adria"
    assert convert.event_folder({"short_name": "FSG", "event_name": "Formula Student Germany"}) == "fs-germany"
    assert convert.event_folder({"short_name": "FSEast", "event_name": ""}) == "fseast"
    assert convert.event_folder({"short_name": "FSG", "event_name": "Formula Student Germany"}, {"FSG": "fsg"}) == "fsg"


def test_to_markdown_turns_breaks_and_scripts_into_text():
    text, images = convert.to_markdown("Area in m<sup>2</sup><br>of V<sub>bat</sub>&nbsp;if x &lt; 5 <b>now</b>")
    assert text == "Area in m^2\nof V_bat if x < 5 now"
    assert images == []


def test_to_markdown_keeps_fs_quiz_images_local_and_others_as_links():
    text, images = convert.to_markdown('See<br><img src="https://img.fs-quiz.eu/testquiz/a b.jpg"> and <img src="https://example.com/x.png">')
    assert "![](images/a_b.jpg)" in text
    assert "![](https://example.com/x.png)" in text
    assert images == ["https://img.fs-quiz.eu/testquiz/a b.jpg"]


def test_to_markdown_does_not_eat_an_escaped_comparison():
    text, _ = convert.to_markdown("a &lt;b&gt; c")
    assert text == "a <b> c"


def test_topics_from_categories_follow_the_flags():
    row = {"math": "1", "mechanical": 1, "electronic": "0", "rule": None}
    assert convert.topics_from_categories(row) == ["math", "mechanics"]
    assert convert.topics_from_categories(None) == []


def test_answer_value_is_text_list_or_none():
    assert convert.answer_value([{"answer_id": 1, "answer_text": " 5 ", "is_correct": True}]) == "5"
    both = [
        {"answer_id": 2, "answer_text": "B", "is_correct": True},
        {"answer_id": 1, "answer_text": "A", "is_correct": True},
    ]
    assert convert.answer_value(both) == ["A", "B"]
    assert convert.answer_value([{"answer_id": 1, "answer_text": "A", "is_correct": False}]) is None


def test_options_only_for_choice_questions_in_answer_id_order():
    answers = [
        {"answer_id": 3, "answer_text": "c", "is_correct": False},
        {"answer_id": 1, "answer_text": "a", "is_correct": True},
    ]
    assert convert.option_texts({"type": "single-choice", "answers": answers}) == ["a", "c"]
    assert convert.option_texts({"type": "input", "answers": answers}) == []


def make_question():
    return {
        "question_id": "12",
        "text": "Q",
        "time": "90",
        "type": "single-choice",
        "answers": [
            {"answer_id": 1, "answer_text": "1 kN", "is_correct": False},
            {"answer_id": 2, "answer_text": "2 kN", "is_correct": True},
        ],
    }


def test_problem_fields_from_api_and_earliest_quiz_year():
    refs = [
        {"quiz_id": 9, "year": 2021, "class": "cv", "position": 4},
        {"quiz_id": 3, "year": 2019, "class": "ev", "position": 1},
    ]
    fields = convert.problem_fields(make_question(), "fsg", refs, ["mechanics"])
    assert fields["id"] == 12
    assert fields["year"] == 2019
    assert fields["rules_year"] == 2019
    assert [ref["quiz_id"] for ref in fields["quizzes"]] == [3, 9]
    assert fields["time_s"] == 90
    assert fields["options"] == ["1 kN", "2 kN"]
    assert fields["answer"] == "2 kN"
    assert fields["status"] == "unverified"
    assert fields["source"] == "https://fs-quiz.eu/question/12"


def test_problem_fields_keep_what_people_edited():
    existing = {"topic": ["physics"], "unit": "kN", "rule_refs": ["T 11.2"], "answer": "stale", "notes": "checked twice"}
    fields = convert.problem_fields(make_question(), "fsg", [], ["mechanics"], existing)
    assert fields["topic"] == ["physics"]
    assert fields["unit"] == "kN"
    assert fields["rule_refs"] == ["T 11.2"]
    assert fields["notes"] == "checked twice"
    # The answer still comes from FS Quiz while the problem is unverified.
    assert fields["answer"] == "2 kN"


@pytest.mark.parametrize("existing, protected", [
    (None, False),
    ({"status": "unverified"}, False),
    ({"status": "verified"}, True),
    ({"status": "unverified", "locked": True}, True),
])
def test_is_protected(existing, protected):
    assert convert.is_protected(existing) is protected


def test_front_matter_round_trip_with_awkward_text():
    fields = convert.problem_fields(make_question(), "fsg", [], [])
    fields["options"] = ['a: "quoted" # not a comment', "ü"]
    fields["answer"] = fields["options"][0]
    text = convert.render_problem(fields, "# Problem 12\n")
    parsed, body = convert.parse_front_matter(text)
    assert parsed == fields
    assert body == "\n# Problem 12\n"


def test_parse_front_matter_without_front_matter():
    assert convert.parse_front_matter("# Just text\n") == ({}, "# Just text\n")


def test_problem_body_lists_images_and_labelled_options():
    body = convert.problem_body(12, "Question?", ["12_1.jpg"], ["1 kN", "2 kN"])
    assert body == "# Problem 12\n\nQuestion?\n\n![](images/12_1.jpg)\n\nOptions:\n- A) 1 kN\n- B) 2 kN\n"


def test_solution_markdown_carries_the_import_marker():
    text, images, inline = convert.solution_markdown(5, [{"solution_id": 1, "text": "Use F = m a", "images": [{"path": "s.png"}]}])
    assert text.startswith(convert.IMPORTED_MARKER)
    assert "Use F = m a" in text and "![](images/s.png)" in text
    assert images == ["s.png"] and inline == []
    assert convert.solution_markdown(5, []) == (None, [], [])
    assert convert.solution_markdown(5, [{"solution_id": 1, "text": "  ", "images": []}]) == (None, [], [])


def test_split_number_reads_comma_decimals():
    assert convert.split_number("6,48 kWh") == (Decimal("6.48"), "kwh")
    assert convert.split_number("A) yes") is None


@pytest.mark.parametrize("printed, expected, match", [
    ("135.0 GPa", "135 GPa", True),
    ("135 gpa", "135 GPa", True),
    ("136 GPa", "135 GPa", False),
    ("6.48", "6.48", True),
    ("6.480", 6.48, True),
    ("6.49", "6.48", False),
    ("0 mm", "0 mm", True),
    ("Yes", "yes", True),
    ("B; A", ["A", "B"], True),
    ("A", ["A", "B"], False),
    ("anything", None, False),
])
def test_answers_match(printed, expected, match):
    assert convert.answers_match(printed, expected) is match
