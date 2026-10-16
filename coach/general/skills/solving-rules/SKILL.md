---
name: solving-rules
description: How to solve a Formula Student quiz question - five rules never to break (answer copied from the script, round once, rules quoted from this year's files, a verdict for every option, exactly one answer with no alternatives), givens and units, Python for every number, rounding (thresholds in the safe direction), answer formats and rule references. Use for every quiz problem.
---

# Solving rules

## Never break these
1. **The answer comes from the script.** Run the script first, then copy the final answer from its last printed line. Never write a number before the script printed it, and never retype or round it by hand afterwards.
2. **Round once, at the end.** Keep full precision in every intermediate value; never feed a rounded value into the next step.
3. **Rules from this year's files, never from memory.** Every rule number, limit, penalty, time or formula you use is found in `general/rules/current/` or `competitions/<event>/handbook/current/` in this session and quoted with its number. Start with `general/rules/KEY-VALUES-<year>.md` and the "Differs from FS Rules" section of `COMPETITION.md`. Values change every year (2026: Skidpad Tmax = 1.35 Tmin, Skidpad cone 0.2 s), so what you remember may be last year's. Can't find it: say so.
4. **Every option gets a verdict.** In a choice question, write true or false for each option with its reason (the rule quote or the computed value) before you choose. Skip none.
5. **Exactly one answer.** Never "X or Y", and no alternative value on the side either ("or 2.37 if the key rounds down"): the live quiz takes one answer and it can't be changed. If two readings of the question remain, give the more likely one, say which reading you used, and lower your confidence. Unsure how to round: settle it with the threshold check in section 4, don't hand the choice to the member.

## 1. Read the question
- Read the whole question, every option and every figure or table before you start: key data are often only in a figure.
- Copy every given value with its unit into a list. Note what is asked and in which unit.
- Note the answer format the question states: decimal places, significant figures, unit, separator, truncate or round. The question wins over `COMPETITION.md`, and `COMPETITION.md` wins over this skill.
- Watch the classic traps: diameter vs radius, kW vs W, km/h vs m/s, rpm vs rad/s, gauge vs absolute pressure, per wheel vs per axle vs per car, mass vs weight, percentages vs fractions.
- If a value is missing, say what you assume and why, then keep going.

## 2. Compute
- Convert every input to SI first. Use the `uncertainty-and-units` skill (pint) when there are several units.
- Every number in the answer comes from Python you actually ran. Keep the script: it is the `solution.py` for this problem and its last line prints the final answer, already rounded and formatted.
- Keep full precision until the last step; round only the final answer.
- Use constants the question or the handbook gives. If none is given, use g = 9.81 m/s² and say so.
- Use `sympy` when you need an exact result, a rearranged formula or to solve an equation.
- No code execution in your agent? Do the arithmetic step by step, keep full precision, and say that it was not run.

## 3. Check
- Units: the result has the unit asked for.
- Plausibility: is it a sensible value for an FS car (mass about 150–300 kg, speed up to about 120 km/h, accumulator up to 600 V, power within the rules' limits)? If not, look for the error before answering.
- Re-read the question once more against your result: did you answer what was asked?

## 4. Round and format
- Never use Python's `round()` for the final answer: it rounds halves to even (`round(0.125, 2)` gives 0.12) and suffers from float storage (`round(2.675, 2)` gives 2.67). Use `Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` from `decimal`, unless the format says otherwise.
- Truncate only when the question or `COMPETITION.md` says truncate.
- **Thresholds round in the safe direction.** When the answer is the least value that still meets a requirement ("minimum", "at least", "required", "needed to reach") round up at the required decimals (`ROUND_CEILING`); when it is the most that is still allowed ("maximum", "at most", "not exceed") round down (`ROUND_FLOOR`). Then put the rounded value back into the condition in the script and check that it still holds. Example: pre-charge to at least 95 % (EV 5.7.1) needs 2.3726 s; 2.37 s stays under 95 %, so the answer is 2.38. The question's own rounding instruction wins over this.
- No format stated anywhere: give 2 decimal places and say the format was not stated.
- Answer types:
  - **single-choice**: exactly one option. Compute or look up the answer, then match the option; don't pick by elimination alone. Still give every option its verdict.
  - **multi-choice**: judge every option on its own as true or false; select all true ones. Watch singular wording ("Which statement is correct?") that still has several correct options. Check `COMPETITION.md` for how wrong picks are scored.
  - **input**: one value in the required format and unit.
  - **input-range**: one value; the quiz accepts a range around the correct result, so precision still matters.

## 5. Rules questions
- Find the rule: by number with a search (`rg -n "D 9.1.1" general/rules/current`), by topic in the index next to each rulebook and handbook (`<name>.index.md`: headings with their page). What changed this year is in `<name>.changes.md`.
- Quote the rule number and its exact text from `general/rules/current/` or the competition handbook. The .md garbles formulas and tables: use `KEY-VALUES-<year>.md` or the PDF page for those.
- The competition handbook wins over FS Rules: check "Differs from FS Rules" in `COMPETITION.md` before applying an FS rule (e.g. FSG 2026 has no Tilt Test).
- Can't find the rule: say so. Never answer a rules question from memory alone.

## 6. The answer you give
1. Final answer, exactly in the required format, copied from the script's last printed line; one value per asked quantity, no alternatives
2. Steps: givens, formula, result (short)
3. Rule references with their quotes, and assumptions
4. Choice questions: the verdict for every option
5. Confidence: high, medium or low, and why
