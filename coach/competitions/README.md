# Competitions

One folder per competition, named after the FS Quiz event: `fsa`, `fs-alpe-adria`, `fsg`, ...

```
<event>/
  COMPETITION.md      quiz rules for this event (written by Gion)
  skills/             this event's calculation and answer rules (written by Gion)
  handbook/current/   this year's handbook (PDF + Markdown); older years in handbook/<year>/, not in the zip
  problems/<id>/      problem.md, solution.py, solution.md (imported from FS Quiz)
```

## COMPETITION.md headings
Gion fills these in for each event:
- Quiz format: number of questions, question types, open-book or not
- Time limit: total and per question
- Decimals and answer format: decimal places, separator, units, rounding or truncation
- Scoring: points, penalties for wrong answers, partial credit on multi-choice
- Submission: how answers are entered, what counts as one attempt
- Event specifics: anything that differs from FS Rules
