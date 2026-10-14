---
name: solving-rules
description: How to solve a Formula Student quiz question - givens and units, Python for every number, rounding, answer formats for single-choice, multi-choice, input and input-range questions, and rule references. Use for every quiz problem.
---

# Solving rules

## 1. Read the question
- Copy every given value with its unit into a list. Note what is asked and in which unit.
- Note the answer format the question states: decimal places, significant figures, unit, separator, truncate or round. The question wins over `COMPETITION.md`, and `COMPETITION.md` wins over this skill.
- Watch the classic traps: diameter vs radius, kW vs W, km/h vs m/s, rpm vs rad/s, gauge vs absolute pressure, per wheel vs per axle vs per car, mass vs weight, percentages vs fractions.
- If a value is missing, say what you assume and why, then keep going.

## 2. Compute
- Convert every input to SI first. Use the `uncertainty-and-units` skill (pint) when there are several units.
- Every number in the answer comes from Python you actually ran. Keep the script: it is the `solution.py` for this problem and it prints the final answer.
- Keep full precision until the last step; round only the final answer.
- Use constants the question or the handbook gives. If none is given, use g = 9.81 m/s² and say so.
- Use `sympy` when you need an exact result, a rearranged formula or to solve an equation.
- No code execution in your agent? Do the arithmetic step by step and say that it was not run.

## 3. Check
- Units: the result has the unit asked for.
- Plausibility: is it a sensible value for an FS car (mass about 150–300 kg, speed up to about 120 km/h, accumulator up to 600 V, power within the rules' limits)? If not, look for the error before answering.
- Re-read the question once more against your result: did you answer what was asked?

## 4. Round and format
- Never use Python's `round()` for the final answer: it rounds halves to even (`round(0.125, 2)` gives 0.12) and suffers from float storage (`round(2.675, 2)` gives 2.67). Use `Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)` from `decimal`, unless the format says otherwise.
- Truncate only when the question or `COMPETITION.md` says truncate.
- No format stated anywhere: give 2 decimal places and say the format was not stated.
- Answer types:
  - **single-choice**: exactly one option. Compute or look up the answer, then match the option; don't pick by elimination alone.
  - **multi-choice**: judge every option on its own as true or false; select all true ones. Check `COMPETITION.md` for how wrong picks are scored.
  - **input**: one value in the required format and unit.
  - **input-range**: one value; the quiz accepts a range around the correct result, so precision still matters.

## 5. Rules questions
- Quote the rule number and its exact text from `general/rules/current/` or the competition handbook.
- For an event procedure, the competition handbook wins over FS Rules.
- Can't find the rule: say so. Never answer a rules question from memory alone.

## 6. The answer you give
1. Final answer, exactly in the required format
2. Steps: givens, formula, result (short)
3. Rule references and assumptions
4. Confidence: high, medium or low, and why
