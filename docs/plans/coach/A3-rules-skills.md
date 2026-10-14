# A3. Rules and skills

## A3.1 General solving rules
Branch: `feat/skill-solving-rules`
- `general/skills/solving-rules/SKILL.md`: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: reviewed by a topic checker.

## A3.2 Log entry skill
Branch: `feat/skill-log-entry`
- `general/skills/log-entry/SKILL.md`: one file per solve `log/<yyyy-mm-dd>-<user>-<problem>.md`
- Fields: problem, agent, result (correct / wrong / unknown), approach, what went wrong, why, rule for next time, status `unreviewed`
- Agents with git push it to `log`; agents without git print it as text
Done when: a sample entry from Claude Code and one from ChatGPT match the format.

## A3.3 Formula library
Branch: `feat/formula-library`. Skill `tdd`.
- `general/tools/`: tested Python functions for recurring formulas (mechanics, electronics, vehicle dynamics), added as problems need them
Done when: pytest passes; `solution.py` files import from it.

## A3.4 Competition rules
One branch per competition: `feat/competition-<event>`
- `COMPETITION.md`: quiz format, decimals, time limit, scoring, answer submission rules
- `skills/`: calculation conventions specific to that competition
Done when: reviewed against that competition's handbook.
