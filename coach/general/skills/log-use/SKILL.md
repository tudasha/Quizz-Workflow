---
name: log-use
description: How to use the team's shared solve log - join the live quiz session, read the other members' answers and the lessons before a question, write an entry after the quick answer, the team answer and every review, and record answers. Use before and after every quiz question.
---

# Using the shared log

The log lives in the team's quiz workflow app. Every member's agent reads and writes it live: during a live quiz it is how the members' agents see each other's answers, and afterwards a mistake one agent logged helps all the others. How to connect is in `LOG.md`.

## Sessions
- Live quiz: one member calls `start_session(competition, year, live: true)` and shares the code it returns; the others call `join_session(code)`. All members are in the same session.
- Practice: `start_session(competition, year)`, alone or shared the same way.
- Every entry carries the session and `question`, the question's number in the quiz.

## Before a question
- `get_answers(session, question)`: every answer, review and feedback the members logged for this question, newest first. Call it again before the team compares (`solve-modes` step 8) and while the question is open (step 12).
- `get_lessons(competition, topic, problem_id?)`: lessons from earlier quizzes and practice. Read `confirmed` lessons first. `unreviewed` entries are hints only; skills, rules and verified problems win over them. Mention in your answer any lesson you used.

## After each answer
Write an entry with `add_log_entry` (`solve-modes`):
- right after the quick answer, with `mode: quick`
- after the team answer, with `mode: team` and `feedback` on every other answer for the question
- after each re-check caused by a new answer, with `mode: review`

| Field | What to write |
|---|---|
| session | the session code |
| question | the question's number in the quiz |
| competition | folder name, e.g. `fs-germany` |
| problem_id | FS Quiz question id for a past problem; `new` in a live quiz |
| question_text | live quiz: the question as the member gave it, in the first entry for it |
| topic | math, physics, mechanics, electronics, rules, marketing, static-events, dynamic-events, scoring |
| agent | agent and model, e.g. `Claude Code, Sonnet 5.5` |
| mode | `quick`, `team` or `review` |
| answer | the answer exactly as given to the member |
| result | `correct`, `wrong`, or `unknown` (always `unknown` during a live quiz) |
| approach | method in one or two sentences |
| what_went_wrong | the mistake, or `nothing` |
| why | the cause, not the symptom |
| rule_for_next_time | one rule another agent can follow, or `none` |
| feedback | why your answer is right, and for each other answer logged for the question whether it is right and why; quick entries: `none` |

- `result` is `correct` or `wrong` only when compared with an official answer: the one in `problem.md` for a past problem, or the results published after a live quiz.
- A recurring trap with no single question (e.g. "FSA gives diameters, not radii") is an entry with `problem_id: note`.
- Never write the member's API token, passwords or personal data in an entry.

## Score
After each quick answer, `record_answer(session, question, answer, time_s)`. Later answers update it.

## Without MCP
Print each entry in this block as soon as it is ready; the member shares it in the team chat during a live quiz and pastes it into the Log entry form in the app. When the member pastes other members' entries, treat them like `get_answers` results.

```yaml
session:
question:
competition:
problem_id:
question_text:
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
