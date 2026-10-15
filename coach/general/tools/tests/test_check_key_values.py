import check_key_values

RULES = "# FS-Rules\n\n<!-- page 1 -->\n\nEV 2.2.1 The TS power at the outlet of the TSAC must not\nexceed 80 kW.\n"


def make_coach(tmp_path, key_values, year=2026, rules=RULES):
    rules_dir = tmp_path / "general" / "rules"
    (rules_dir / "current").mkdir(parents=True)
    (rules_dir / "current" / "FS-Rules.md").write_text(rules, encoding="utf-8")
    (rules_dir / "current" / "FS-Rules.index.md").write_text("- Power limit, p. 1\n", encoding="utf-8")
    (rules_dir / ("KEY-VALUES-" + str(year) + ".md")).write_text(key_values, encoding="utf-8")
    return tmp_path


def test_quotes_found_across_line_breaks_pass(tmp_path):
    coach = make_coach(tmp_path, '- Power: 80 kW [EV 2.2.1: "must not exceed 80 kW."]\n')
    assert check_key_values.problems(coach, 2026) == []


def test_a_quote_missing_from_the_rules_fails(tmp_path):
    coach = make_coach(tmp_path, '- Power: 75 kW [EV 2.2.1: "must not exceed 75 kW."]\n')
    assert check_key_values.problems(coach, 2026) == [
        'KEY-VALUES-2026.md: quote not in the current rules: "must not exceed 75 kW."'
    ]


def test_quotes_are_not_looked_up_in_the_index(tmp_path):
    coach = make_coach(tmp_path, '- Limit [EV 2.2.1: "Power limit, p. 1"]\n')
    assert len(check_key_values.problems(coach, 2026)) == 1


def test_last_years_file_fails_in_a_new_year(tmp_path):
    coach = make_coach(tmp_path, '- Power: 80 kW [EV 2.2.1: "exceed 80 kW."]\n', year=2026)
    assert check_key_values.problems(coach, 2027) == [
        "KEY-VALUES-2026.md: not this year's file; update it for 2027 and rename it",
        "KEY-VALUES-2027.md is missing",
    ]
