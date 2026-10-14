# A5. Trial and review

## A5.1 Trial
- 2–3 members on different agents (Claude Code, Codex, a Claude Project or ChatGPT with the zip) solve real problems for a week
Done when: each agent produced log entries in the right format.

## A5.2 Log review
- Topic checkers mark entries `confirmed` or `rejected`
- A lesson that repeats goes into a skill through a PR to `main`

## A5.3 Scoring
Branch: `feat/scoring`
- Script runs an agent over the test set and reports the score per topic
- Baseline score recorded; re-run after every skill change, the score must rise or hold

## A5.4 Review gate — **Gion**
- Gion reviews the coach repo and the trial results
- After approval, work moves to the quiz app (steps 1–8)
