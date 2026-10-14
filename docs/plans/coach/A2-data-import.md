# A2. Data import

## A2.1 Permission — **Gion**
- Ask the FS Quiz site owner for permission or an export (quizzes, answers, solutions)
Done when: written permission or an export file exists. Nothing is scraped before this.

## A2.2 Problem format
Branch: `feat/problem-format`
- `problem.md` front matter: id, event, year, topic, type, answer_format, answer, unit, rule_refs, source, status (`unverified` | `verified`), verified_by
- Body: problem text, images next to it
- `solution.py` prints the final answer; `solution.md` explains the approach
- JSON schema for the front matter, checked by CI
Done when: two hand-made example problems pass CI.

## A2.3 Import script
Branch: `feat/import`. After A2.1 and A2.2.
- `general/tools/import/` turns the export into `competitions/<event>/problems/<id>/`
- Imported answers get `status: unverified`
- Script is re-runnable and does not overwrite verified problems
Done when: import of the export runs without errors and CI passes.

## A2.4 Rules and handbooks
Branch: `feat/rules-handbooks`
- FS Rules in `general/rules/<version>/`, each competition handbook in `competitions/<event>/handbook/<year>/` (Markdown where possible, PDF kept beside it)
Done when: every competition folder has its current handbook.

## A2.5 Verification
Not code; topic checkers.
- Check imported answers per topic, set `status: verified` and `verified_by` via PRs
## A2.6 Test set
- Pick about 100 verified problems across topics and competitions
- Store them outside this repo (private repo or Gion's drive) so agents never see them
