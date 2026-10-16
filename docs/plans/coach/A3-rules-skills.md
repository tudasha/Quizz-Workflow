# A3. Rules and skills

Gion, 2026-10-14: Claude writes `AGENTS.md`, the general skills (A3.1, A3.2, A3.5, A3.6) and, since 21:59, each competition's `COMPETITION.md` from the pattern of its past quizzes and its handbook (A3.4); Gion reviews them. Competition `skills/` still come from Gion's text: agents format it, keep the wording and ask about gaps instead of filling them.

## A3.1 General solving rules — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solving-rules/SKILL.md`. Topics: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: Gion has reviewed it.

## A3.2 Log use skill — done
Done in `feat/coach-agent-files`; tool names follow A4.3.
- `coach/general/skills/log-use/SKILL.md`: join the shared live session; before each question, read every member's answers to it and the lessons for its topic; write an entry after the quick answer, the team answer and each review
- Entry fields: session, question number, problem (or the question text in a live quiz), agent, mode (quick / team / review), answer, result (correct / wrong / unknown; unknown during a live quiz), approach, what went wrong, why, rule for next time, feedback (which of the other answers are right and why)
- How: MCP tools when the agent supports them, otherwise print the entry for the member to paste into the app form
Done when: Gion has reviewed it.

## A3.3 Shared calculation scripts
Moved to A6.3: filled from solved problems after the trial, not written up front.

## A3.5 Quick and team answers — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solve-modes/SKILL.md`: both modes on every question, made for the live quiz where nobody knows the answer yet (Gion, 2026-10-14). Members join one live session. A quick answer from one agent, logged at once, and a team of 2–3 sub-agents started at the same moment (Gion, 2026-10-16: separate solves, the quick one for questions with little time, the team one more exact and later) that solves independently, compares its answer with every answer the other members logged for that question, and logs which is right and why; each new disagreeing answer triggers a re-check and a review entry, until the answers agree or time is up; the agent says what to submit. Practice on past problems works the same way, with the FS Quiz answer used only afterwards. Web chats do the same steps one after another
Done when: Gion has reviewed it.

## A3.6 Practice quiz maker — done
Gion, 2026-10-14.
- `coach/general/skills/quiz-maker/SKILL.md`: makes a practice quiz for one competition in its own style (types, topics, time limits and answer format from `COMPETITION.md`, the handbook's quiz section and its past problems): variants of past problems, rules questions with rule numbers, new calculations; options built from real mistakes; every answer from Python and checked by a blind second solve; run one question at a time or as a sheet, scored in a practice session. Generated questions never go into `problems/` or the test set
Done when: Gion has reviewed it.

## A3.4 Competition rules
Branch: `feat/competition-md` (all five competitions).
- `COMPETITION.md` per competition, written by Claude (Gion, 2026-10-14): the pattern of its past FS Quiz questions (format, types, time, answer format, recurring topics and traps, with example problem ids) and its 2026 handbook's quiz rules, every fact with its source
- Each file starts with "When something is new": the question wins over the pattern; in a live quiz a question of a new kind is said, solved from the question and current rules, re-checked and logged as a note; before a live quiz check the newest handbook and the organiser's announcement; re-check the file when the import brings a new handbook or new questions
- Competition `skills/`: from Gion's text, when Gion has some
Done when: Gion has reviewed the five files.

## A3.7 Review fixes — done
Gion, 2026-10-15, from the Gemini and Claude reviews of the zip. Branch: `feat/strict-rules-and-key-values`.
- `solving-rules` starts with five rules never to break: the answer is copied from the script, round once, rules quoted from this year's files, a verdict for every option, exactly one answer
- `general/rules/KEY-VALUES-<year>.md`: limits, penalties and scoring formulas with rule and quote; CI checks every quote against the current rules
- Each `COMPETITION.md` starts with "Differs from FS Rules": where its handbook changes FS Rules, every point checked against both texts
- `quiz-maker`: works without the app, SVG figures, questions in English
- References to files that are not in the zip removed or marked
Done when: Gion has reviewed it.
