---
name: log-use
description: How to use the team's shared solve log - read lessons and other answers before a problem, write an entry after the quick answer and another after the team answer, and record answers in a solve session. Use before and after every quiz problem.
---

# Using the shared log

The log lives in the team's quiz workflow app. Every member's agent reads and writes it live, so a mistake one agent logs helps all the others. How to connect is in `LOG.md`.

## Before a problem
- Call `get_lessons(competition, problem_id, topic)`. Without a problem id (a new question), use the competition and topic. It returns the lessons and every answer already logged for the problem, by any member.
- Read `confirmed` lessons first. `unreviewed` entries are hints only; skills, rules and verified problems win over them.
- Mention in your answer any lesson you used.
- Call it again before the team compares answers (`solve-modes` step 8): other members may have logged this problem meanwhile.

## After a problem
Write two entries for every problem, right or wrong, with `add_log_entry` (`solve-modes`):
- right after the quick answer, with `mode: quick`
- after the team answer, with `mode: team` and `feedback` on every other answer for the problem

| Field | What to write |
|---|---|
| competition | folder name, e.g. `fs-germany` |
| problem_id | FS Quiz question id, or `new` plus the question text |
| topic | math, physics, mechanics, electronics, rules, marketing, static-events, dynamic-events, scoring |
| agent | agent and model, e.g. `Claude Code, Sonnet 5.5` |
| mode | `quick` or `team` |
| answer | the answer exactly as given to the member |
| result | `correct`, `wrong`, or `unknown` (no official answer yet) |
| approach | method in one or two sentences |
| what_went_wrong | the mistake, or `nothing` |
| why | the cause, not the symptom |
| rule_for_next_time | one rule another agent can follow, or `none` |
| feedback | team entries: why the correct answer is right, and for each other answer in the log whether it is right and why; quick entries: `none` |

- `result` is `correct` or `wrong` only when compared with the official answer in `problem.md` or given by the member.
- A recurring trap with no single problem (e.g. "FSA gives diameters, not radii") is an entry with `problem_id: note`.
- Never write the member's API token, passwords or personal data in an entry.

## Quiz runs
- At the start of a quiz or practice set: `start_session(competition, year)`.
- After each quick answer: `record_answer(session, problem_id, answer, correct, time_s)`, then the quick log entry. The team answer goes in the team log entry.

## Without MCP
Print each entry in this block, the quick one right after the quick answer and the team one at the end; the member pastes them into the Log entry form in the app.

```yaml
competition:
problem_id:
topic:
agent:
mode:
answer:
result:
approach:
what_went_wrong:
why:
rule_for_next_time:
feedback:
```
