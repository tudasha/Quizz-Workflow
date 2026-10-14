# Formula Student Balkans — registration quiz

Pattern from the FS Quiz history (2024 and 2026, 31 questions, 0 with a written solution) and the 2026 handbook (FSBalkan_2026_Competition_Handbook_v0.2.md, "Registration Procedure" and "The Registration Quiz", p.7). Written by Claude on 2026-10-14; reviewed by: pending.

## When something is new
This file is the pattern of past quizzes and the 2026 handbook: a guide, not a rule.
- The question wins. If it asks for another type, unit, number of decimals or separator than this file says, follow the question and tell the member it differs from the usual pattern.
- Live quiz: when a question is of a kind this file does not cover (new type, new topic, new answer format, a scoring or submission detail not listed here), say so, solve it from the question and the current rules and handbook, and re-check your answer once more before giving it. Then log a note (`log-use`, `problem_id: note`) naming this competition and what was new, so a maintainer updates this file.
- Before a live quiz: check that `handbook/current/` is the newest handbook version and read the organiser's latest quiz announcement and FAQ. Where they differ from this file, they win; tell the member and log a note.
- When the weekly import brings a new handbook or new quiz questions for this competition, re-check this file against them.

## Quiz format
- Citations: the handbook (HB) has no rule numbers, so it is cited as [HB p.N section]; FS Rules 2026 v1.1 by rule number
- All 31 FS Quiz answers are status "unverified"; none has a written solution [FS Quiz 2024–2026]
- Online form on the FSBk website; it also asks team name, university, class, car number and invoice details [HB p.7 The Registration Quiz]
- Content: "common engineering knowledge and good understanding of the formula student rules" [HB p.7 The Registration Quiz]
- The 2026 quiz opened 29 January 2026 19:00 CET [HB p.7 The Registration Quiz]; that date has passed, the next edition's date: Not stated: check the quiz announcement
- Questions per quiz: 2024 = 20, 2026 = 11; no 2025 quiz in the data [FS Quiz 2024–2026]
- FS Quiz lists an EV and a CV quiz each year, but both hold the same questions at the same positions (all 31 problems) [FS Quiz 2024–2026]
- So both classes get CV and EV questions: pneumatic shifter 733 and compression ratio 995 in the EV quiz, accumulator 997 in the CV quiz [FS Quiz 2024–2026]
- No DV quiz: no Driverless class at FSBk2026 [HB p.4 Competition Format]; separate quiz for Alumni or Class 2: Not stated: check the quiz announcement
- Types: 2024 = 16 single-choice + 4 numeric input; 2026 = 11 single-choice (100 %) [FS Quiz 2024–2026]
- Single-choice has 4 options (5 once, 740); several values are often packed into one option, e.g. "Cx = 0.07; Cz = 1.35" [FS Quiz 2024–2026]
- 7 of 31 come with an image (chart, circuit, gear train, beam, lever): 725, 736, 741, 744, 994, 998, 1084 [FS Quiz 2024–2026]
- Open-book or not, tools allowed: Not stated: check the quiz announcement

## Time limit
- Total: Not stated: check the quiz announcement
- Per question: Not stated: check the quiz announcement (FS Quiz records no time limit for this event) [FS Quiz 2024–2026]
- Speed counts: teams are ranked on submission time and accuracy [HB p.7 Registration Procedure]
- Protests open 29 January 23:00 CET, 4 h after the start [HB p.7 The Registration Quiz]

## Decimals and answer format
- Input answers (2024 only): all 4 keyed with 2 decimals, trailing zeros kept: "71.00", "13.49", "111.40", "3600.00" [FS Quiz 2024–2026]
- Each input prompt says "(answer format round to nearest decimal eg:12.34)": round to 2 decimals, point as separator [FS Quiz 2024–2026]
- No units in input answers; single-choice options carry units in the text ("135 GPa", "t = 9.028 mm") [FS Quiz 2024–2026]
- Separators are mixed in question text: "0,1 mm" (995), option "1.300 GPa" (938); read by context [FS Quiz 2024–2026]
- Options can be truncated rather than rounded: 739 team B computes to 86.78, option shows 86.7; pick the nearest option [FS Quiz 2024–2026]
- Rounding vs truncation rule: Not stated: check the quiz announcement
- No multiple-choice (several correct) seen; "which are not ..." is still single-choice (731) [FS Quiz 2024–2026]

## Scoring
- Ranking on submission time and accuracy of the answers [HB p.7 Registration Procedure]
- Points per question, wrong-answer penalty, partial credit, time bonus, tie-break: Not stated: check the quiz announcement
- Proforma invoice goes to the first applicants; payment due 4 February 2026 [HB p.7 Registration Procedure], 23:59 [HB p.9 Registration Fees]
- 5–13 February 2026: registration open to all applicants until slots are filled; registered teams published 14 February [HB p.7 Registration Procedure]
- Slots: 15 CV (incl. hybrid), 15 EV (no hydrogen), 5 CV/EV Alumni; each class is a separate competition if at least 6 teams register [HB p.4 Competition Format]
- Fees: CV/EV €2450, Class 2 (Concept) €1000, Alumni €1500 [HB p.9 Registration Fees]
- Protests 29 January 23:00 to 30 January 23:00 CET to contact@fsbalkans.ro; results and quiz answers published 31 January 12:00 CET [HB p.7 The Registration Quiz]

## Submission
- Prerequisites: team account on the FSBk website and an active FSG team account [HB p.7 Registration Procedure]
- A submission is completing the form; its time is a ranking factor [HB p.7 Registration Procedure]
- Who may answer, how many people: Not stated: check the quiz announcement
- Number of attempts, changing answers, late entry: Not stated: check the quiz announcement
- Desired car number is given at registration: E### EV, ### CV, HY### hybrid, striped ### Alumni [HB p.7 Car Number]

## What they ask
Topic shares, 31 questions, total (2024 / 2026) [FS Quiz 2024–2026]:
- mechanics 8 (5 / 3): statics, gears, strength of materials, ICE, tolerances
- physics 5 (4 / 1): gas laws, humidity, falling body with drag, aero polar
- electronics 4 (2 / 2), rules 4 (2 / 2), scoring 3 (2 / 1)
- static-events 2 (2 / 0), dynamic-events 2 (2 / 0), math 1 (1 / 0)
- other 2 (0 / 2): FSBk trivia and local culture; marketing 0

Recurring themes [FS Quiz 2024–2026]:
- Dynamic-event points for 2–4 listed teams, one option holds all scores: 739, 740, 999
- Endurance procedure: tyre change on wet/damp track, driver change: 742, 743
- Static-event rules: BPP finals points, cost report BOM category: 728, 726
- FS electrical rules: LV voltage limit, BSPD: 735, 734
- Gas law with real conditions (mmHg, °C, tyre or gas bottle): 727, 733
- ICE: knock, compression ratio, shifter gas use: 731, 995, 733
- Strength of materials and statics: 938, 994, 725
- Electrical calculation: resistivity, temperature coefficient, energy from accumulators: 730, 732, 997
- Reading a figure: airfoil polar 1084, logic circuit 998, gear train 736
- FSBk handbook, event trivia, Transylvanian culture: 990, 996, 991, 993
- Long humorous "Balkan" story with surplus data: 725, 744, 997

Traps [FS Quiz 2024–2026]:
- Scoring follows the quiz year's rules: 739 (2024) key matches 0.95·Pmax·(Tmax/Tteam − 1)/(Tmax/Tmin − 1) + 0.05·Pmax with Tmax = 1.25·Tmin, 740 (2024) has efficiency max 75; 2026 rules use the quadratic D 9.1.1 / D 9.4.1 and FSBk max points [HB p.28 Scoring System]
- 999 key (100 / 28.8 / 2 / 23.5) is closest to CV and EV cars pooled in one efficiency ranking (100 / 29.3 / 2.0 / 23.6); per class (100 / 29.3 / 59.9 / 100) matches no option: compute both
- Efficiency fuel: litres × 0.79 kg/L ÷ 1.45 for E85, litres × 0.75 kg/L for RON98 [HB p.26–27 Efficiency Measurement]
- Last-step offsets: 995 subtract the 0.1 mm thinner gasket (1.372 mm is the distractor); 744 E85 is 85 % ethanol
- Unstated constants: 730 needs nichrome resistivity (key implies 1.0×10⁻⁶ Ω·m)
- Efficiency chains: 997 key (3 cars) is reached only by applying both the 90 % inverter and the 70 % grill efficiency
- Surplus data: 733 temperature; 728 number of presenters (finalists score 71–75 regardless, FS Rules 2026 S 2.4.7)
- Notation: Cx = drag, Cz = lift coefficient (1084); 729 names ISO 2768-mK but asks the fine class (±0.1; medium ±0.2 is also offered)
- A self-made fastener is a "part" in the BOM (726, FS Rules 2026 S 3.4.6)
- Sloppy options: negative wording and two identical options in 731
- Handbook questions are not verbatim: 996's key is not in HB v0.2, the other options are contradicted by [HB p.11 Campsite Rules]: eliminate
- 727 key (0.50 bar) could not be reproduced: isochoric gas law gives about 1.05 bar gauge; keys are unverified

## Event specifics
- The handbook supersedes FS Rules 2026 v1.1 where they conflict [HB p.3 Applicable Rules]
- Quiz rules refer to FS Rules only in general ("good understanding of the formula student rules") [HB p.7 The Registration Quiz]
- No transponders: laser timing, no reflective surfaces in its path (asked in 990) [HB p.8 Transponders]
- No Driverless class; DV rules void (T 14, T 15, IN 6, IN 11.2) [HB p.4 Competition Format; HB p.28–29 Rule Exemptions]
- Max points differ from FS Rules Table 3: Skidpad 75, Acceleration 75, Endurance 325, Efficiency 100 (FS Rules: 50 / 50 / 250 / 75); BPP 75, C&M 100, ED 150, Autocross 100 unchanged [HB p.28 Scoring System]
- 25 points for every team finishing Endurance without DNF or DQ [HB p.26 Endurance and Efficiency Scoring]
- Fixed fuel densities, no team-declared values; HB cites "D7.10.4" for E85 ÷ 1.45, which is D 7.9.4 in FS Rules 2026 v1.1 [HB p.26–27 Efficiency Measurement]
- Running out of order: 2 min penalty [HB p.25 Running Out of Order; FS Rules 2026 D 10.2.1]
- Autocross: rolling start, 1 timed + 1 untimed lap, 4 runs by 2 drivers [HB p.24–25 Autocross Event]
- Acceleration: timing beam broken after 0.30 m of travel [HB p.24 Acceleration Event]
- EV accumulators may follow FS Rules 2025 v1.1 or 2026 v1.1 EV 5.8 [HB p.29 Electric Vehicle Accumulator Requirements]
- 4 to 6 registered drivers per team [HB p.30 Driver Requirements]
- Campsite: no vehicles except loading, campervans only if approved, no motorcycles or scooters, quiet hours and no speakers over 100 W after 00:00 [HB p.11 Campsite Rules & Safety]
- Rules the questions cite (FS Rules 2026): T 11.1.2 LV max 60 VDC / 50 VAC RMS (735); T 11.6 BSPD, 500 ms, supplied directly from LVMS (734); D 7.5 and D 10.2.5 driver change, up to 2 min penalty (743); D 7.6 Table 10 tyre changes (742); S 2.4.7 (728); S 3.4.6 (726); D 9.1.1 and D 10.1.7 cones 2 s (739); D 9.4 (999)
