# Formula Student Alpe Adria — registration quiz

Pattern from the FS Quiz history (2023, 2024 and 2026, 43 questions, 24 with a written solution) and the 2026 handbook (FSAA2026_Competition_Handbook_v1.0.md, III.5 FSAA 2026 Quiz Registration, pages 7–8). Written by Claude on 2026-10-14; reviewed by: pending.

## When something is new
This file is the pattern of past quizzes and the 2026 handbook: a guide, not a rule.
- The question wins. If it asks for another type, unit, number of decimals or separator than this file says, follow the question and tell the member it differs from the usual pattern.
- Live quiz: when a question is of a kind this file does not cover (new type, new topic, new answer format, a scoring or submission detail not listed here), say so, solve it from the question and the current rules and handbook, and re-check your answer once more before giving it. Then log a note (`log-use`, `problem_id: note`) naming this competition and what was new, so a maintainer updates this file.
- Before a live quiz: check that `handbook/current/` is the newest handbook version and read the organiser's latest quiz announcement and FAQ. Where they differ from this file, they win; tell the member and log a note.
- When the weekly import brings a new handbook or new quiz questions for this competition, re-check this file against them.

## Quiz format
- 2026: one joint quiz with Formula Student Poland (FSP), linked on both the FSAA and FSP platforms; teams select the event they want inside the quiz [Handbook III.5]
- The quiz section is numbered III.5 although it sits in chapter II (Registration and Eligibility) [Handbook III.5]
- Questions per quiz: 14 in 2023, 15 in 2024 (3 later removed: 855, 857, 864), 14 in 2026; FS Quiz has no FSAA quiz for 2025 [FS Quiz 2023–2026]
- Classes: FSAA 2026 runs CV (hybrids included) and EV, no DV [Handbook I.1]
- FS Quiz lists one quiz (labelled EV) in 2023 and 2024, and an EV and a CV quiz in 2026 with the same 14 questions in the same order: expect one common question set [FS Quiz 2023–2026]
- Types 2026: 12 input, 1 input-range, 1 single-choice (13 of 14 typed answers) [FS Quiz 2023–2026]
- Types 2024: 12 input, 1 single-choice, 1 multi-choice, 1 written explanation [FS Quiz 2023–2026]
- Types 2023: 7 input, 5 single-choice, 2 PDF uploads (hand drawing, sponsor handout) [FS Quiz 2023–2026]
- Uploads and free-text parts show in FS Quiz as one placeholder option "(This answer is correct)": 623, 625, 861, parts 1 and 3 of 865 [FS Quiz 2023–2026]
- Multi-part questions: 11 of 43 put 2–7 values in one answer box (6 of 14 in 2026) [FS Quiz 2023–2026]
- Chained questions: 631 builds on 629, 1068 on 1067 [FS Quiz 2023–2026]
- Open-book, tools, outside help: Not stated: check the quiz announcement
- Questions have needed outside material: a data file for an FFT (622), Google Maps (635), a STEP file plus FEA (1066), maker datasheets by URL (1070) [FS Quiz 2023–2026]

## Time limit
- 2026: quiz on 30 January 2026, 17:00 CET, "will remain open for 45 minutes" [Handbook III.5]
- Whether 45 minutes is the answering time or only the window to open the quiz: Not stated: check the quiz announcement
- Per question: Not stated: check the quiz announcement
- 14 questions in 45 minutes is about 3 minutes per question; 2026 included FEA and datasheet work, so triage the long ones [derived from Handbook III.5 and FS Quiz 2023–2026]
- FS Quiz holds no time data for this event [FS Quiz 2023–2026]
- Dates are for 2026 (handbook v1.0 released 15.01.2026); later quizzes: check the new handbook [Handbook changelog]

## Decimals and answer format
- Decimal separator: comma. All 26 decimal values stored for 2024 and 2026 use a comma [FS Quiz 2023–2026]
- 1058: "Write with commas instead of dots, without the units of measurement"; 1067 and 1068: dots in the figure are to be read as commas [FS Quiz 2023–2026]
- 2023 answers are stored with dots (61.17, 35.5), but 2023 texts use commas (20,23 mV/g) and 626 asks for "X,XXX; Y,YYY; Z,ZZZ": use the comma [FS Quiz 2023–2026]
- Decimal places are stated in every numeric question but one (856) [FS Quiz 2023–2026]
- Seen per numeric value: 0 dp 16, 1 dp 7, 2 dp 15, 3 dp 9, 4 dp 1; plus 13 text values [FS Quiz 2023–2026]
- Keep trailing zeros the question asks for: "0,10 x A" (1060), "8,40" (1069) [FS Quiz 2023–2026]
- Rounding: always "round" to nearest; truncation never asked; odd steps occur: nearest 5 Hz (622), nearest cm (853), "three or four decimal places" (1068) [FS Quiz 2023–2026]
- Units are not typed; the question names the unit and scale: N, s, kJ, ms, kWh, "millions of mm4", "grams * square millimeters" [FS Quiz 2023–2026]
- Several values, 2026: separated by ", " (comma and space) in the order of the "Answer: a, b, c" line, e.g. "29,87, 133,86, 35,352" (1058) [FS Quiz 2023–2026]
- Several values, 2023–2024: separated by "; " per "Answer format: {Part 1}; {Part 2}", e.g. "0,98; 156,9" (856), "5.800; 14.768; 30.750" (626) [FS Quiz 2023–2026]
- Special formats: "[number] x [parameter]" as "0,10 x A" (1060); "[x,xx] x [Yes/No]" as "8,40 x No" (1069); a set in ascending order "X, X, …" (854); a path "X-X-X" (865); film titles (1059); a symbolic transfer function (1061) [FS Quiz 2023–2026]
- Multi-choice (only 866): "Multiple correct answers are possible and all of them need to be marked"; options lettered a)–f) [FS Quiz 2023–2026]
- Single-choice: 3–5 options, sometimes "None of the above" or "Remains Invariable" [FS Quiz 2023–2026]

## Scoring
- Points per question, penalty for wrong answers, partial credit on multi-choice or multi-value answers, time bonus, tie-break: Not stated: check the quiz announcement
- How the quiz result maps to registration slots: Not stated: check the quiz announcement
- Slots 2026: 25 CV (incl. HY), 45 EV, 10 Alumni [Handbook I.1]
- Reserved: 3 slots per class for the FSAA 2025 top finishers; all teams from Croatia, Slovenia, Bosnia and Herzegovina and Serbia; Rennteam Stuttgart; Arrabona Racing Team [Handbook III.4]
- Whether reserved teams must still take the quiz: Not stated: check the quiz announcement
- Alumni teams contact the organisers (fee €500, up to 10 members) [Handbook II.1]
- After registration results, confirmed teams pay €4,500 by 4 February 2026; unpaid slots go to the next team on the waiting list [Handbook II.1]
- Waiting-list teams must still upload all documents by the deadlines [Handbook V.3]
- Organisers have accepted alternatives or tolerance bands (635: 118 or 122; 854: two sets; 864: "tolerance in the answer"; 1070: 70-80 ms) and removed flawed questions (855, 857, 864) [FS Quiz 2023–2026]
- 2023 upload graded by hand: "judged by accuracy and aesthetics" (623) [FS Quiz 2023–2026]

## Submission
- Before the quiz: register on the platform of the event you aim for; for both FSP and FSAA, register on both with the same email, team name and university name [Handbook III.5]
- Create the account(s) at least 24 hours before the quiz [Handbook III.5]
- All older accounts were deleted; the team leader creates and activates the account, then registers the team (Team Info → Register your team → Update Team Info) [Handbook III.6]
- Teams must also be registered on the FSG website [Handbook I.1]
- In the quiz, select your desired event (participation option) [Handbook III.5]
- Who answers (team leader or several members), number of attempts, changing answers, late entry, what counts as submitted: Not stated: check the quiz announcement
- 2023 uploads: named Drawing_UniversityName.pdf / Handout_UniversityName.pdf, max 10 MB [FS Quiz 2023–2026]

## What they ask
- Topic shares, 43 questions (own classification): mechanics 17 (40 %), physics 11 (26 %), electronics 6 (14 %), other 3 (7 %), math 2 (5 %), rules 2 (5 %), scoring 1 (2 %), marketing 1 (2 %), static-events 0, dynamic-events 0 [FS Quiz 2023–2026]
- 2026 alone: mechanics 6, physics 5, electronics 2, other 1; no rules, scoring or marketing question [FS Quiz 2023–2026]

Recurring themes [FS Quiz 2023–2026]:
- Aero coefficients (SCx, SCz, DRS, air density, coast-down, wing drag): 629, 856, 1063
- Load transfer and tyre loads (CoG height, anti-dive, cornering): 627, 858, 1065
- Hydraulics (pump, pistons, relief and flow control valves): 628, 861, 1060
- Tolerances and GD&T (1D stack-up, dowel pins, ISO GPS): 626, 1067, 1068
- Strength and section properties (shaft sizing, area moments, FEA von Mises): 859, 1058, 1066
- Thermodynamics and heat (Joule cycle, calorimetry, brake disc heating): 860, 1062, 1071
- EV energy and electrical (acceleration energy with regen, fuse clearing time, motor losses): 863, 1070, 855
- Control systems (P gain with filter delay, block diagram transfer function): 864, 1061
- FS rules compliance "which is true" for a given car spec: 634, 866
- Maths and operations puzzles (sphere volume, knapsack, critical path): 853, 854, 865
- Points strategy and non-technical: 624 (endurance vs efficiency points), 625 (sponsor handout), 1059 (films with gears)

Recurring traps [FS Quiz 2023–2026]:
- Decimal comma and value separator are the same character in 2026: "29,87, 133,86"; follow the answer line exactly
- Scaled units: millions of mm4 (1058), g·mm² (1066), kJ (1062), ms (1070); inputs in mA, kOhm, uOhm (855)
- Values to take from the rules, not given: FSG maximum permitted voltage (855), minimum ground clearance (867), 1,2 m aero height (866)
- Percent wording: "by 8000% larger than" (867); sign convention "from the cold store's point of view" gives negatives (860)
- Physical rounding: laps rounded up to a whole lap (635: 117,3 → 118); energy budget counts only the discharge of the last run (863)
- Symmetry collapses parts: 1066 asks inertia about x, y, z but stores one value for a)
- Stored answers can drop the asked decimals (855: 388,8 for two decimals; 862: 1 for one decimal): follow the question
- Data files use decimal commas: convert before computing (622 solution)
- FS Quiz text has PDF-copy garble ("p = 3 1,225 kg/m", "at = A 3 m, s"): check the images

## Event specifics
- Quiz shared with FS Poland; one quiz, event chosen inside it [Handbook III.5]
- The handbook overrides FS Rules 2026 (v1.1) where they differ [Handbook V.1]
- FSAA points: BPP 75, Cost 100, Design 150, Skidpad 75, Acceleration 75, Autocross 100, Endurance 325, Efficiency 100, total 1000 (use for points-strategy questions like 624) [Handbook V.1]
- Handbook deviations from FS Rules: BPP 10 minutes replacing S 2.2.5, S 2.1.2 not applied [Handbook VII.1]; Design event per FS Rules 2025 S 3 except S 3.1.3, S 3.4.7, S 3.7.2 [Handbook VII.3]; accumulators per EV5.8 of 2025 v1.1 or 2026 v1.1 [Handbook VI.1]
- Rejected protest costs 15 points [Handbook V.1]; 4 runs by 2 drivers in Acceleration, Skidpad, Autocross [Handbook VIII.3]; 2-minute penalty for out-of-order Endurance [Handbook VIII.4]
- Rules cited by past questions (older rule years; check numbers in general/rules/current/): T 2.8 and T 2.9 wheelbase and track (634, 2023), T 6.1.2 two hydraulic brake circuits (866, FSG Rules 2024 v1.1), aero devices below 1,2 m behind the head restraint (866), FSG maximum permitted voltage (855), minimum ground clearance (867) [FS Quiz 2023–2026]
- Non-FS sources cited: F1 2022 rules (635); ISO 8015, ISO 14405, ISO 22081, ISO 13715, ISO 21920-1, DIN 7979 (1067, 1068); ISO 7200 title block (623) [FS Quiz 2023–2026]
