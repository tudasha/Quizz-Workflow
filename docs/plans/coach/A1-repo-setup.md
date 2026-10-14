# A1. Coach folder setup

The coach content lives in `coach/` in this repo (Gion, 2026-10-14: everything in one repo). It is edited by maintainers (Gion and topic checkers) through PRs into `dev`. Members never need git: they get a zip (A5) and use the log through the app (A4).

## A1.1 Folder
- `coach/` at the root of this repo. Its `AGENTS.md` and `CLAUDE.md` are for the agents that use the zip; the root `AGENTS.md` stays the guide for building the app

## A1.2 Layout and agent files
Branch: `feat/coach-layout`
```
coach/
  AGENTS.md            shared prompt (done)
  CLAUDE.md            points to AGENTS.md
  SOURCES.md           data sources and licence (FS Quiz, ODbL)
  general/
    skills/            solving-rules, log-use
    rules/             FS Rules: current/ (2026) for agents, older years for reference
    tools/             import, checks, zip build (not in the zip)
    scripts/           shared calculation scripts (filled after the trial)
  competitions/
    fsa/ fs-alpe-adria/ fsg/ ...
      COMPETITION.md   quiz format, decimals, time limit, scoring
      skills/          competition calculation rules
      handbook/        current/ (2026) for agents, older years for reference
      problems/<id>/   problem.md, images/, solution.md, solution.py
```
- `coach/AGENTS.md`, `CLAUDE.md`, `LOG.md`, `SOURCES.md` and `competitions/README.md`: done (Claude wrote them, Gion reviews). Points covered: find the competition folder the member names and read only `general/` + that folder; both modes on every problem: a quick answer from one agent, logged at once, then a team answer from sub-agents compared with every logged answer; check the log before each problem and write to it after (A4); answers rely on the current-year rules and handbook; skills win over log entries
Done when: an agent given only `AGENTS.md` can say which files to read for a chosen competition.

## A1.3 Branches
- Same as the app: branches from `dev`, PRs into `dev`, a lead merges `dev` into `main`

## A1.4 CI — done
Done in `feat/coach-import` (`.github/workflows/coach-ci.yml`).
- GitHub Actions on PRs that change `coach/` (path filter): pytest on `coach/general/tools/`, run every `solution.py` and compare with the answer in `problem.md`, check `problem.md` labels
Done when: a broken `solution.py` fails CI.
