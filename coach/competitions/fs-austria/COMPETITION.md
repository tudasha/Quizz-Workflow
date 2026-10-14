# Formula Student Austria — registration quiz

Pattern from the FS Quiz history (2014, 2016–2026, 187 questions, 25 with a written solution) and the 2026 handbook (FSA-Competition-Handbook-2026-V1.1.1.md, AT 2 Registration & Eligibility). Written by Claude on 2026-10-14; reviewed by: pending.

## When something is new
This file is the pattern of past quizzes and the 2026 handbook: a guide, not a rule.
- The question wins. If it asks for another type, unit, number of decimals or separator than this file says, follow the question and tell the member it differs from the usual pattern.
- Live quiz: when a question is of a kind this file does not cover (new type, new topic, new answer format, a scoring or submission detail not listed here), say so, solve it from the question and the current rules and handbook, and re-check your answer once more before giving it. Then log a note (`log-use`, `problem_id: note`) naming this competition and what was new, so a maintainer updates this file.
- Before a live quiz: check that `handbook/current/` is the newest handbook version and read the organiser's latest quiz announcement and FAQ. Where they differ from this file, they win; tell the member and log a note.
- When the weekly import brings a new handbook or new quiz questions for this competition, re-check this file against them.

## Quiz format
- Separate quizzes for EV and CV since 2017; 2014 and 2016 have only an EV quiz in the data [FS Quiz 2014–2026].
- No DV quiz: FSA runs only the classes EV and CV, with no driverless class and no Driverless Cup [HB AT 1.6, AT 1.8].
- Class EV = EV and FCEV; class CV = CV, HY, H2CV and H2HY [HB AT 1.1].
- Questions per quiz (EV/CV): 2017 14/14, 2018 14/15, 2019 16/14, 2020 15/15, 2021 19/20, 2022 12/12, 2023 15/15, 2024 17/17, 2025 12/12, 2026 12/11 [FS Quiz 2017–2026].
- Most questions appear in both quizzes; in 2023–2026 each class had 0–1 questions of its own (EV: 662, 840, 1082; CV: 661, 839) [FS Quiz 2023–2026].
- Types 2023–2026: single-choice 52 of 58 (90%), input 6 (10%); 2026 alone: 9 single-choice, 3 input [FS Quiz 2023–2026].
- All years: single-choice 162, input 24, input-range 1 (2020) [FS Quiz 2014–2026].
- Single-choice questions have 2–8 options, mostly 4 (39 of 52 in 2023–2026) [FS Quiz 2023–2026].
- 10 of 58 questions in 2023–2026 put the data in a figure or table image [FS Quiz 2023–2026].
- Open-book, tools, calculators: Not stated: check the quiz announcement.
- Several questions need rule values for a calculation (655, 826, 835), so keep FS Rules and the handbook at hand if allowed [FS Quiz 2023–2024].

## Time limit
- Total and per-question limits: Not stated: check the quiz announcement (the handbook gives only the start time) [HB AT 2.1].
- FS Quiz stores a separate time per question (time_s) for FSA quizzes from 2020 on, none before; whether each question has its own timer is Not stated: check the quiz announcement [FS Quiz 2014–2026].
- Sum of question times per quiz: 2023 2460 s (41 min, one question per quiz without a time), 2024 4140 s (69 min), 2025 2820 s (47 min), 2026 EV 2300 s / CV 2290 s (38 min) [FS Quiz 2023–2026].
- Single-choice: 10–700 s, median 180 s (n=50) in 2023–2026; 10–900 s, median 145 s (n=88) in 2020–2026 [FS Quiz 2020–2026].
- Input: 180–480 s, median 195 s (n=6) in 2023–2026; 180–600 s, median 300 s (n=15) in 2020–2026 [FS Quiz 2020–2026].
- Input-range: 600 s (n=1) [FS Quiz 2020].
- 120 s is the most common time (34 questions), used for short rule lookups [FS Quiz 2020–2026].
- Long calculations and multi-statement rule questions get 400–700 s (910, 918, 1078) [FS Quiz 2025–2026].
- Trivia and quick-read items got 10–40 s (1076, 1077, 1082) [FS Quiz 2026].

## Decimals and answer format
- Input answers by decimal places: 0 dp 6, 1 dp 6, 2 dp 11, 3 dp 1, plus one range answer (6.4-6.6, question 359) [FS Quiz 2018–2026].
- 2023–2026 inputs: 2 dp three times (830, 840, 1072), 1 dp once (649), integers for the two puzzles (1075, 1079) [FS Quiz 2023–2026].
- Every calculation input states its rounding ("round to two digit after the decimal points", "Round to nearest integer", "rounded to 0.01"); only rounding is seen, never truncation [FS Quiz 2018–2026].
- Some calculations say to use full precision for intermediate results (470, 473) [FS Quiz 2018].
- Decimal separator: dot. 18 of 25 input questions add "Please use the following format: 12.34" [FS Quiz 2019–2026].
- That format line shows the separator, not the decimals: integer answers come with the same line (130 → 59, 456 → 29, 1079 → 35) [FS Quiz 2021–2026].
- Trailing zeros are kept to the asked decimals: 649 → 5.0, 151 → 7.30 [FS Quiz 2021, 2023].
- Comma decimals appear only in 2016 option text (64: "1,41g", "35,3°") [FS Quiz 2016].
- Input answers are a bare number; the unit is named in the question ("in cm3", "in kg", "Answer in kilonewtons") [FS Quiz 2018–2026].
- Choice options carry the unit ("57 points", "48.1 kph", "6.7 mm") [FS Quiz 2023–2024].
- No input asks for several values; choice options combine them ("Front: 44 N/mm, Rear: 76 N/mm" in 910, "Yes, dropped at h=18.13 m" in 835, "sigma=28.5MPa, delta da=0.00078mm" in 362) [FS Quiz 2020–2025].
- Choice questions are single-choice: pick one option. Only 64 (2016) had two accepted options; there is no multiple-choice type at FSA [FS Quiz 2014–2026].
- Whether the input field accepts a comma, a unit or extra decimals: Not stated: check the quiz announcement.

## Scoring
- Points per question, penalty for wrong answers, partial credit, time bonus: Not stated: check the quiz announcement.
- Ranking: "Registrations will be given out in the order of the quiz results and afterward in the order of submission." [HB AT 2.3]
- Tie-break: only the "order of submission" phrase above; whether submission time breaks equal scores is Not stated: check the quiz announcement [HB AT 2.3].
- Slots: 58 in total, 40 EV / 18 CV; later entries go to a waiting list; slots may move between classes [HB AT 2.3].
- Reserved slots, assigned automatically: 3 per class for the listed top finishers, 7 for the listed Austrian teams, up to 3 wildcard and up to 3 hydrogen slots [HB AT 2.3.2–2.3.4].
- A team that fits several reserved slots takes the one listed first; a reservation expires unless the team is registered on the FSA website when the quiz starts [HB AT 2.3.1].
- Wildcard and hydrogen slots need the "Wildcard & Hydrogen Application" before registration starts [HB AT 2.3.4].
- After getting a slot: fee EUR 4730 incl. VAT, paid within 3 working days of the invoice, or the slot is lost and the team goes to the waiting list [HB AT 2.2].

## Submission
- Quiz start for FSA 2026: Friday 2026-01-30, 19:00 CET; details on the FSA website [HB AT 2.1].
- FSA 2027 quiz date: Not stated: check the quiz announcement.
- Register the team on fsaustria.at at least one day before the quiz starts [HB AT 2.1].
- Who answers (one account per team, how many people): Not stated: check the quiz announcement.
- One attempt or several, changing answers, going back to earlier questions: Not stated: check the quiz announcement.
- Late entry and what counts as a submission: Not stated: check the quiz announcement; the order of submission is used after the quiz results [HB AT 2.3].

## What they ask
Topic shares, all years (187) and 2023–2026 (58), Claude's classification of every question because FS Quiz labels are missing for 2018 and 2022–2026 [FS Quiz 2014–2026]:
- Rules and handbook knowledge, no calculation: 48% (89) / 52% (30)
- Engineering calculation (mechanics, vehicle dynamics, thermodynamics, electrics): 25% (46) / 22% (13)
- Engineering concept or reading a plot or circuit, no calculation: 16% (30) / 7% (4)
- Calculation that needs a rule value: 6% (11) / 5% (3)
- Scoring or penalty calculation: 3% (6) / 7% (4)
- Puzzles and trivia: 3% (5) / 7% (4)
- FS Quiz labels on the 97 labelled questions, several per question: rules 42, math 31, mechanics 28, electronics 21, dynamic-events 16, static-events 7, scoring 3 [FS Quiz 2014–2021].

Recurring themes [FS Quiz 2014–2026, weighted to 2023–2026]:
- Penalties: endurance corrected time (DOO, missed slalom, out-of-order, flags, post-run violations) and post-inspection weight change (824, 911, 825)
- Dynamic event score from run times (656, 647, 22)
- Business Plan Presentation at FSA: pitch video, judging, finalist and non-finalist scores, link to the car (652, 658, 836)
- FSA handbook items: powertrain classes, TSAL green sign, extinguishers, design judging (920, 1073, 919)
- Impact attenuator and anti-intrusion plate (909, 835, 660)
- Harness, lap belt and driver equipment (917, 831, 145)
- Fasteners, bonded joints and frame tube materials (829, 654, 1081)
- Brakes: brake rules, brake test, brake balance, caliper sizing (913, 918, 147)
- Vehicle dynamics and aero calculations: ride height under downforce, banked turn, pitch stiffness, cornering speed (826, 828, 910)
- EV electrics: accumulator container rules, battery current and power, filters and inverters (662, 912, 840)
- Campsite and cat stories wrapped around physics (830, 648, 459)
- Puzzles and trivia, new weight in 2026: crossword, hex sequence, pattern series, cat trivia (1075, 1079, 1083)

Recurring traps:
- Negated stems ("incorrect", "not permitted", "must not") in about 1 of 10 questions (829, 917, 1081) [FS Quiz 2024–2026].
- The quiz tests where FSA overrides FS Rules: no "TSAL green" sign is needed at FSA (1073) because AT 4.12 replaces FS Rules A 6.9.2 [HB AT 4.12].
- 1080 asks whether a sensor placement is "OK in 2026 at FSA"; FSA accepts EV5.8 of 2025 v1.1 or 2026 v1.1 [HB AT 4.11].
- Values change by year: the pitch video was max 30 s in 2023 (652) but is max 90 s in 2026 [HB AT 5.4.3].
- The 2021 BPP answer 63.1 (131) becomes 63.0 with the 2026 non-finalist formula 71 · P_your / P_min-F [HB AT 5.8.2].
- Dynamic scoring changed: FS Rules 2026 use one unified formula with Tmax and Pmin from Table 11; older answers (22, 647, 656) used older formulas [FS Rules 2026 D 9.1.1].
- Weight change penalty is 20 points per started kg beyond ±5 kg: 7.3 kg gives 60, not 46 (825) [FS Rules 2026 IN 12.1.7].
- A small broken-off part such as a piece of front wing endplate is not a lost-part DQ at FSA (824) [HB AT 4.10].
- Mixed units in the givens: inch, kph, hp, Gal, ft/s, bar (146, 456, 465) [FS Quiz 2021–2022].
- Use the constants the question gives: 146 was deleted because the options used another g than the question's 9.80665 [FS Quiz 2021].
- Data sits in images: run times (647), sketch (830), circuit (840) [FS Quiz 2023–2024].

## Event specifics
- The handbook's quiz rules cover only start time, pre-registration and ranking to slots; the quiz format is left to the FSA website [HB AT 2.1, AT 2.3].
- Only EV and CV classes, so no DV quiz; slot split 40 EV / 18 CV [HB AT 1.6, AT 1.8, AT 2.3].
- The handbook supersedes FS Rules 2026 where they differ [HB AT 1.2]; 2–3 questions per recent quiz hinge on the FSA handbook (2023: 651, 652, 658; 2024: 824, 836; 2025: 919, 920; 2026: 1073, 1080) [FS Quiz 2023–2026].
- Handbook rules behind past questions: AT 1.1 powertrains (920), AT 1.8.1 autonomous parts (454), AT 1.8.2 4–6 drivers where FS Rules D 1.2.1 say 3–4 (106), AT 4.9 extinguishers (916), AT 4.10 lost parts (824), AT 4.12 working on EVs (1073), AT 5 BPP (652, 658, 836), AT 7.1 design judging (919), AT 8.2 endurance running order (824) [HB 2026].
- FS Rules chapters the questions often test: T 3 chassis incl. IA/AIP, T 5 driver restraint, T 6 brakes, T 10 fasteners, T 13 driver equipment and extinguishers, IN 11 brake test, IN 12 post inspection, D 9 scoring, D 10 penalties, EV 5 accumulator [FS Quiz 2023–2026].
- AT 8.2.3 cites "Rules 2026/D9.2.1" for the out-of-order penalty, but in FS Rules 2026 v1.1 it is D 10.2.1 (2 min) [HB AT 8.2.3, FS Rules 2026 D 10.2.1].
- Questions often say "at FSA <year>" or use the FSA campsite and the FSA cat; answer them with that year's FSA handbook [FS Quiz 2021–2026].
