# A3. Rules and skills

Content comes from Gion. Agents do not write these rules or skills from scratch: they turn Gion's text into the file format (SKILL.md front matter, headings), keep the wording, and ask about gaps instead of filling them. Tasks marked **Gion** wait for that text.

## A3.1 General solving rules — **Gion**
Branch: `feat/skill-solving-rules`
- `general/skills/solving-rules/SKILL.md` from Gion's text. Expected topics: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: Gion confirms the file says what they wrote.

## A3.2 Log entry skill — **Gion**
Branch: `feat/skill-log-entry`
- `general/skills/log-entry/SKILL.md`: one file per solve `log/<yyyy-mm-dd>-<user>-<problem>.md`
- Fields: problem, agent, result (correct / wrong / unknown), approach, what went wrong, why, rule for next time, status `unreviewed`
- Agents with git push it to `log`; agents without git print it as text
Done when: a sample entry from Claude Code and one from ChatGPT match the format.

## A3.3 Formula library
Branch: `feat/formula-library`. Skill `tdd`.
- `general/tools/`: tested Python functions for recurring formulas (mechanics, electronics, vehicle dynamics), added as problems need them
Done when: pytest passes; `solution.py` files import from it.

## A3.4 Competition rules — **Gion**
One branch per competition: `feat/competition-<event>`
- `COMPETITION.md` and `skills/` from Gion's text. Expected topics: quiz format, decimals, time limit, scoring, answer submission rules
- `skills/`: calculation conventions specific to that competition
Done when: reviewed against that competition's handbook.
