# Coach tools

For maintainers. Not shipped in the zip.

| File | Does |
|---|---|
| `fsquiz/` | Imports problems, solutions and images from the FS Quiz API, and the current-year FS Rules and handbooks |
| `check_problems.py` | CI check: `problem.md` labels (`problem.schema.json`), linked images, and every `solution.py` against its answer |
| `check_key_values.py` | CI check: every quote in `general/rules/KEY-VALUES-<year>.md` is still in this year's FS Rules |
| `build_zip.py` | Builds `fs-quiz-coach.zip` (and one zip per competition when it is too big), and the web chat files |
| `chat_files.py` | For web chats that can't open a zip: per competition `fs-quiz-coach-<event>-chat.md` (AGENTS.md, skills, COMPETITION.md, key values), `-handbook-<year>.md` and `-problems.md`, plus one `fs-quiz-coach-rules-<year>.md` |
| `config.json` | Current year, which quizzes and events to import, folder names, zip size limit |

## Run locally
FS Quiz must be reachable from your machine (it is blocked in Claude's cloud sessions).
```bash
cd coach/general/tools
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q                       # tool tests
python -m fsquiz all                      # problems + rules and handbooks
python check_problems.py                  # what CI checks
python check_key_values.py
python build_zip.py --out ../../../dist   # the zip and chat files, in dist/ (ignored by git)
```
`python -m fsquiz problems` or `documents` runs one half. Answers are cached for a day in `.cache/`; `--no-cache` asks again.
`python -m fsquiz convert` needs no API: it converts the rules and handbooks in `current/` again from their PDFs, the ones an older converter made (`converter` in `documents.json`), or all with `--force`. Raise `CONVERTER_VERSION` in `fsquiz/docs.py` when the conversion changes; the next import then converts them again too.

## config.json
- `current_year`: the rules and handbooks agents use. Change it when next season's FS Rules come out; the old files move to `<year>/` folders on the next import.
- `quiz_statuses`: FS Quiz quiz statuses to import (`complete`, `missing_questions`, `missing_correct_answer`, `incomplete`).
- `events`: competitions to import, each by its exact FS Quiz short name (`FSG`) or part of its full name (`Alpe Adria`); empty means all. Now: Alpe Adria, Austria, Germany, Balkans, Greece (Gion, 2026-10-14). `skip_events` leaves some out. Each import lists the events it took and the ones it left out.
- `folder_names`: a different folder for an event, by short name, e.g. `{"FSG": "fsg"}`. Without it the folder comes from the full name: `Formula Student Alpe Adria` becomes `fs-alpe-adria`.
- `document_types`: FS Quiz document types for `general/rules/` and for each competition's `handbook/`.
- `zip_split_above_mb`: above this size the build also makes one zip per competition.

## What the import keeps
- A problem with `status: verified` or `locked: true` is never rewritten.
- `topic`, `unit`, `rule_refs`, `rules_year`, `status`, `verified_by` and any extra field you add stay as you set them.
- `solution.md` is refreshed only while its first line is the import marker; delete that line to keep your edits. `solution.py` is never written by the import.
- Problems that disappear from FS Quiz are not deleted.

## GitHub Actions
- **Coach import** (`.github/workflows/coach-import.yml`): runs every Monday, on demand, and when these tools change on `dev`. It imports, runs the checks and opens or refreshes one PR from `feat/coach-data-import` into `dev`. On a PR that changes the tools it only does a dry run. Needs *Settings → Actions → General → Allow GitHub Actions to create and approve pull requests*.
- **Coach CI** (`coach-ci.yml`): on PRs that touch `coach/`: tests, `check_problems.py`, and a preview zip under the run's artifacts.
- **Coach zip** (`coach-zip.yml`): on pushes to `main` that touch `coach/`: builds the zip and the chat files and replaces the files of the `coach-latest` release, so the download links stay the same: `https://github.com/tudasha/Quizz-Workflow/releases/download/coach-latest/fs-quiz-coach.zip`, and the same address with a chat file's name instead of the zip's.
