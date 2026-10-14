# A6. Trial and review

## A6.1 Trial
- 2–3 members on different agents (Claude Project, ChatGPT, Gemini, Claude Code) load a zip, connect the log and solve real problems for a week
Done when: every agent read and wrote log entries.

## A6.2 Scoring
Branch: `feat/scoring`
- Script runs an agent over the test set and reports the score per topic
- Baseline score recorded; re-run after every skill change, the score must rise or hold

## A6.3 Shared calculation scripts
Branch: `feat/shared-scripts`. After A6.1. Skill `tdd`.
- Scripts that several `solution.py` files repeat move to `coach/general/scripts/` with tests, so agents reuse them instead of rewriting
Done when: pytest passes; the repeated solutions import from `coach/general/scripts/`.

## A6.4 Review gate — **Gion**
- Gion reviews `coach/`, the log and the trial results
- After approval, work moves to the rest of the app (Part B)
