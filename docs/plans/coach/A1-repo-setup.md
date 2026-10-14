# A1. Coach repo setup

## A1.1 Create the repo — **Gion**
- Create an empty private repo on GitHub (default name: `fs-quiz-coach`)

## A1.2 Layout and agent files
Branch: `feat/layout`
```
AGENTS.md            shared prompt: order of work, folders to read, when to log
CLAUDE.md            points to AGENTS.md
general/
  skills/            solving-rules, log-entry
  rules/             FS Rules, by version
  tools/             formula library, checks
competitions/
  fsa/ fs-alpe-adria/ fsg/ ...
    COMPETITION.md   quiz format, decimals, time limit, scoring
    skills/          competition calculation rules
    handbook/        by year
    problems/<id>/   problem.md, solution.py, solution.md
log/                 one file per solve (log branch only)
```
- `AGENTS.md` from Gion's text; expected points: read `general/` + one competition folder; solve with Python in `solution.py` style; skills win over log entries; pull before each problem, write a log entry after each one
Done when: an agent given only `AGENTS.md` can say which files to read for a chosen competition.

## A1.3 Branches
Not code; Gion does it on GitHub.
- Protect `main`: PR required, 1 approval, CI must pass
- Create `log` branch; direct pushes allowed for members with access

## A1.4 CI
Branch: `feat/ci`. After A1.2.
- GitHub Actions on PRs into `main`: pytest on `general/tools/`, run every `solution.py` and compare with the answer in `problem.md`, check `problem.md` labels
Done when: a broken `solution.py` fails CI.
