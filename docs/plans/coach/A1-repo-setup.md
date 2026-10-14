# A1. Coach repo setup

The coach repo is edited only by maintainers (Gion and topic checkers). Members never need git: they get a zip (A5) and use the log through the app (A4).

## A1.1 Create the repo — **Gion**
- Create an empty private repo on GitHub (default name: `fs-quiz-coach`)

## A1.2 Layout and agent files
Branch: `feat/layout`
```
AGENTS.md            shared prompt (from Gion's text)
CLAUDE.md            points to AGENTS.md
SOURCES.md           data sources and licence (FS Quiz, ODbL)
general/
  skills/            solving-rules, log-use
  rules/             FS Rules: current/ (2026) for agents, older years for reference
  tools/             import script, checks
  scripts/           shared calculation scripts (filled after the trial)
competitions/
  fsa/ fs-alpe-adria/ fsg/ ...
    COMPETITION.md   quiz format, decimals, time limit, scoring
    skills/          competition calculation rules
    handbook/        current/ (2026) for agents, older years for reference
    problems/<id>/   problem.md, solution.py, solution.md
```
- `AGENTS.md` from Gion's text; expected points: find the competition folder the member names and read only `general/` + that folder; two modes: quick (one agent alone, for easy questions under quiz time) and deep (a coordinator with sub-agents, using the quick answer as a reference); check the log before each problem and write to it after (A4); answers rely on the current-year rules and handbook; skills win over log entries
Done when: an agent given only `AGENTS.md` can say which files to read for a chosen competition.

## A1.3 Branches
Not code; Gion does it on GitHub.
- Protect `main`: PR required, 1 approval, CI must pass

## A1.4 CI
Branch: `feat/ci`. After A1.2.
- GitHub Actions on PRs into `main`: pytest on `general/tools/`, run every `solution.py` and compare with the answer in `problem.md`, check `problem.md` labels
Done when: a broken `solution.py` fails CI.
