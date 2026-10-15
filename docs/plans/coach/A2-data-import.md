# A2. Data import from FS Quiz

Source: FS Quiz API v2, `https://api.fs-quiz.eu/2/` (public, no key; OpenAPI spec in github.com/otti-ai/fs-quiz.eu `api/doku/fs-quiz-api-v2.json`).
Licence: Open Database License (ODbL): credit FS Quiz, and a shared derived database stays under ODbL.

| Endpoint | Gives |
|---|---|
| `/event`, `/event/{id}/quizzes` | events (short_name, country) and their quizzes |
| `/quiz`, `/quiz/{id}/questions` | quizzes (year, class ev/cv/dv, status) and their questions |
| `/question/{id}` | text, type (single-choice, multi-choice, input, input-range), time limit, answers with `is_correct`, solutions, images |
| `/solution/question/{id}` | written solutions with images |
| `/image/{id}` | question and solution images (img.fs-quiz.eu) |
| `/document`, `/quiz/{id}/documents` | rulebooks, handbooks, registration procedures, by event, year and version |

## A2.1 Licence and courtesy note — **Gion**
- `coach/SOURCES.md` with the FS Quiz credit and ODbL terms: done
- Tell the FS Quiz owner how the data is used (courtesy, not a blocker)

## A2.2 Problem format — done
Done in `feat/coach-import`; described in `coach/competitions/README.md`.
- `problem.md` front matter: id (FS Quiz question_id), event, year, quizzes (quiz_id, year, class, position), type, time_s, topic, options, answer, unit, rule_refs, rules_year, source, status (`unverified` | `verified`), verified_by, locked
- Body: question text; images saved next to it
- `solution.md`: FS Quiz solution text when there is one; `solution.py`: written later, prints the final answer
- JSON schema for the front matter (`general/tools/problem.schema.json`), checked by CI
Done when: two hand-made example problems pass CI (covered by the tool tests).

## A2.3 Import script — done, first real run pending
Done in `feat/coach-import`: `general/tools/fsquiz/`, run by the Coach import Action.
- Pulls events, quizzes, questions, answers, solutions and images from the API into `competitions/<event>/problems/<question_id>/`
- Maps event short_name to the competition folder; a question used in several quizzes is stored once and lists all of them
- Skips quizzes whose status is not `complete` unless `config.json` says otherwise; marks every imported answer `unverified`
- Re-runnable: never overwrites verified problems or hand-written files
- Runs where api.fs-quiz.eu is reachable (laptop or a GitHub Action); cached responses so the API is not hammered
Done when: a full import runs without errors and CI passes.

## A2.4 Rules and handbooks — done, first real run pending
Done in `feat/coach-import` (`python -m fsquiz documents`).
- Current year (2026) is the source agents rely on: FS Rules 2026 in `general/rules/current/`, each competition's 2026 handbook in `competitions/<event>/handbook/current/`; PDF plus a Markdown conversion
- 2026 documents come from the API `/document` (the fs-quiz.eu GitHub repo `doc/` only goes up to 2025) or the event websites
- Older years stay in the repo under `rules/<year>/` and `handbook/<year>/`, not in the zip; they are used only when checking an old problem whose answer depended on an older rule (`rules_year` in `problem.md`)
- Cleaner conversion (review, 2026-10-15): no running headers, split small caps or ligatures, rule numbers written "D 9.1.1"; `<name>.index.md` from the PDF bookmarks and `<name>.changes.md` from the changelog. `python -m fsquiz convert` redoes it from the PDFs without the API
Done when: every competition folder has its 2026 handbook in Markdown, and `general/rules/current/` holds FS Rules 2026.

## A2.8 Weekly check — done
Done in `feat/coach-import`: the Coach import Action runs every Monday for problems and documents.
- Scheduled GitHub Action (weekly) asks the FS Quiz API for new problems and new current-year rulebook or handbook versions
- When one appears: download it, convert to Markdown, move the old version to `<year>/`, open a PR into `dev`
- A maintainer approves; the merge rebuilds the zips (A5.1)
Done when: a fake new version in a test run opens a PR.

## A2.5 Topic labels
- Each problem gets a `topic` (math, physics, mechanics, electronics, rules, marketing...); the import suggests it from FS Quiz categories, topic checkers confirm

## A2.6 Verification
Not code; topic checkers.
- Check imported answers per topic, set `status: verified` and `verified_by` via PRs

## A2.7 Test set
- Pick about 100 verified problems across topics and competitions
- Store them outside this repo (Gion's private storage) so agents never see them
