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
- Add `SOURCES.md` with the FS Quiz credit and ODbL terms
- Tell the FS Quiz owner how the data is used (courtesy, not a blocker)

## A2.2 Problem format
Branch: `feat/problem-format`
- `problem.md` front matter: id (FS Quiz question_id), event, year, quiz_id, class, topic, type, time_s, options, answer, unit, rule_refs, source, status (`unverified` | `verified`), verified_by
- Body: question text; images saved next to it
- `solution.md`: FS Quiz solution text when there is one; `solution.py`: written later, prints the final answer
- JSON schema for the front matter, checked by CI
Done when: two hand-made example problems pass CI.

## A2.3 Import script
Branch: `feat/import`. After A2.2.
- `general/tools/import/fsquiz.py`: pulls events, quizzes, questions, answers, solutions and images from the API into `competitions/<event>/problems/<question_id>/`
- Maps event short_name to the competition folder; a question used in several quizzes is stored once and lists all of them
- Skips quizzes whose status is not `complete` unless asked; marks every imported answer `unverified`
- Re-runnable: never overwrites verified problems or hand-written files
- Runs where api.fs-quiz.eu is reachable (laptop or a GitHub Action); cached responses so the API is not hammered
Done when: a full import runs without errors and CI passes.

## A2.4 Rules and handbooks
Branch: `feat/rules-handbooks`. After A2.3.
- Download documents from `/document` (the same PDFs are in the fs-quiz.eu GitHub repo `doc/`, up to 2025)
- FS Rules in `general/rules/<year>/`, handbooks in `competitions/<event>/handbook/<year>/`; PDF plus a Markdown conversion for agents
Done when: every competition folder has its current handbook in Markdown.

## A2.5 Topic labels
- Each problem gets a `topic` (math, physics, mechanics, electronics, rules, marketing...); script suggests, topic checkers confirm

## A2.6 Verification
Not code; topic checkers.
- Check imported answers per topic, set `status: verified` and `verified_by` via PRs

## A2.7 Test set
- Pick about 100 verified problems across topics and competitions
- Store them outside this repo (Gion's private storage) so agents never see them
