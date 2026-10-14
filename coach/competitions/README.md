# Competitions

One folder per competition, named after the event's FS Quiz short name in lower case (`fsg`, `fsa`, ...). A different name can be set in `general/tools/config.json`.

```
<event>/
  COMPETITION.md      quiz rules for this event (written by Gion)
  skills/             this event's calculation and answer rules (written by Gion)
  handbook/current/   this year's handbook (PDF + Markdown); older years in handbook/<year>/, not in the zip
  problems/<id>/      problem.md, images/, solution.md (imported from FS Quiz), solution.py (written by a checker)
```

## COMPETITION.md headings
Gion fills these in for each event:
- Quiz format: number of questions, question types, open-book or not
- Time limit: total and per question
- Decimals and answer format: decimal places, separator, units, rounding or truncation
- Scoring: points, penalties for wrong answers, partial credit on multi-choice
- Submission: how answers are entered, what counts as one attempt
- Event specifics: anything that differs from FS Rules

## problem.md
Front matter, checked by CI against `general/tools/problem.schema.json`:
- From FS Quiz: `id` (question id), `event`, `year` (first quiz year), `quizzes` (quiz id, year, class, position), `type`, `time_s`, `options`, `answer`, `source`
- Kept as checkers set them: `topic` (suggested from FS Quiz categories), `unit`, `rule_refs`, `rules_year`, `status` (`unverified` or `verified`), `verified_by`, `locked`
- `answer` is the FS Quiz answer: one text, or a list when several options are correct. It stays `unverified` until a topic checker confirms it and sets `verified_by`.

## solution.py
- Prints the final answer on its last line, as it would be entered: `135 GPa`, `6.48`; several options separated by `;`.
- CI runs it and compares that line with `answer` (numbers by value, text ignoring case).
