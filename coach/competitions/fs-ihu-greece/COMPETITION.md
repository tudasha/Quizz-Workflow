# Formula IHU (Formula Student IHU, Greece) — registration quiz

Pattern from the FS Quiz history (2024 and 2026, 32 questions, 2 with a written solution) and the 2026 handbook (Formula_IHU_2026_Competition_Handbook_v1.0.md, Formula_IHU_2026_Grey_Areas_Clarification.md; Handbook sections 2.2–2.3). Written by Claude on 2026-10-14; reviewed by: pending.

## When something is new
This file is the pattern of past quizzes and the 2026 handbook: a guide, not a rule.
- The question wins. If it asks for another type, unit, number of decimals or separator than this file says, follow the question and tell the member it differs from the usual pattern.
- Live quiz: when a question is of a kind this file does not cover (new type, new topic, new answer format, a scoring or submission detail not listed here), say so, solve it from the question and the current rules and handbook, and re-check your answer once more before giving it. Then log a note (`log-use`, `problem_id: note`) naming this competition and what was new, so a maintainer updates this file.
- Before a live quiz: check that `handbook/current/` is the newest handbook version and read the organiser's latest quiz announcement and FAQ. Where they differ from this file, they win; tell the member and log a note.
- When the weekly import brings a new handbook or new quiz questions for this competition, re-check this file against them.

## Quiz format
- 10 to 20 questions per quiz [Handbook 2.3].
- 2024: one EV quiz with 15 questions; no CV quiz in the data [FS Quiz 2024].
- 2025: no quiz in the data [FS Quiz 2024–2026].
- 2026: separate EV and CV quizzes, 17 questions each, the same questions in the same order; only the points of the electronics questions 975–978 differ by class [FS Quiz 2026].
- Classes: EV and CV only, no driverless [Handbook 1.2].
- Types: 2024 single-choice 15/15 (100%); 2026 input 9/17 (53%), single-choice 8/17 (47%) [FS Quiz 2024–2026].
- No multiple-choice (several correct options) question seen [FS Quiz 2024–2026].
- Questions come in chains: a follow-up reuses the previous question's data or result (983→984, 985→986, 988→989) [FS Quiz 2026].
- Open-book: Not stated: check the quiz announcement.
- Tools allowed: Not stated: check the quiz announcement.
- In practice the questions need web lookups (973 Formula IHU's first Instagram post, 974 handbook release date), FS Rules and the Grey Areas file (980, 982, 983), a linked PDF drawing likely rebuilt in CAD (988, 989: "MMGS" units and SolidWorks-style material names) and data images (978, 979) [FS Quiz 2024–2026].

## Time limit
- Total: 2 hours; the quiz opens on fihu.gr at 13:00 CET; reload the page if it does not appear (2026: 29-01-2026) [Handbook 2.2.1].
- 13:00 CET is 14:00 Athens time in winter (EET, UTC+2) [derived from Handbook 2.2.1, 1.6.2].
- Per question: Not stated: check the quiz announcement. FS Quiz lists no time limit for this event [FS Quiz 2024–2026].
- Average budget: 2 h / 17 questions ≈ 7 min per question [derived from Handbook 2.2.1, FS Quiz 2026].
- Submission time is recorded automatically and breaks ties: submit as soon as the answers are final [Handbook 2.3].

## Decimals and answer format
- Each input question states its own rounding and an example: "round to 2 decimals, e.g., 145.31", "round to the nearest integer", "nearest one decimal place" [FS Quiz 2026].
- Decimal places in stored input answers: 2 in 5 of 9 (979, 981, 983, 988, 989), 1 in 1 (982), 0 in 2 (974, 984), text in 1 (978) [FS Quiz 2026].
- Trailing zeros kept ("273.40", "72.90"); exceptions: 984 asks for 2 decimals but stores "0", 978 asks "XX.X" but stores "59" [FS Quiz 2026].
- Decimal separator: a point in every input answer and example [FS Quiz 2026]; 2024 options and some givens used a comma ("129,38%", "-7,1%", "μ = 1,5"), and 987 (2026) gives "1,5mm" [FS Quiz 2024–2026]. Handbook: Not stated: check the quiz announcement.
- Units: never in the input answer; the question names the unit [FS Quiz 2026].
- Several values in one answer: comma + space in the order asked ("820.69, 75.27" in 988, 989); labelled values when the format asks for them ("R_{FPGA_CLK}=66.5, R_{FPGA_MOSI}=59, R_{MCU_MISO}=61.9" in 978) [FS Quiz 2026].
- Rounding vs truncation: the questions say "round" (to nearest) [FS Quiz 2024–2026]; the handbook: Not stated: check the quiz announcement.
- Tolerance on input answers: Not stated: check the quiz announcement.
- Choice questions: single-choice, 3 to 6 options; some options bundle two answers ("B / Common Base", "σmax=181 MPa | K=3.667 N/mm", "ZR = 0.02 ohms, I(t)= 100 A"), so both halves must be right [FS Quiz 2024–2026].
- A "not answer" option exists for skipping a question [Handbook 2.3].

## Scoring
- Correct answer: the question's points, which vary with complexity [Handbook 2.3]; 2026 questions print their points in the text, 2 to 8 [FS Quiz 2026].
- 2026 totals from the printed points: EV 69, CV 60 (65 and 58 without the removed 975); electronics 975–978 pay EV 3–6, CV 2 each [FS Quiz 2026].
- Biggest 2026 questions: 979 dynamic-event points (8), 988 CAD assembly (7), 978 termination resistors (EV 6) [FS Quiz 2026].
- Wrong answer: minus half the question's points [Handbook 2.3].
- Blank or "not answer": no change [Handbook 2.3].
- Answer only if P(correct) > 1/3; a blind guess among 4 options loses 1/8 of the points on average [derived from Handbook 2.3].
- Partial credit (e.g. one of two values right): Not stated: check the quiz announcement.
- Time bonus: none stated; time only breaks ties, faster submission ranks higher [Handbook 2.3].
- Team selection and order come from the quiz [Handbook 2.2]; slots: 15 CV and 15 EV teams [Handbook 1.2].
- 14 pre-registered teams (12 Greek, 2 Cypriot) still take the quiz [Handbook 2.3.3, 2.4]; their class split and the open slots left: Not stated: check the quiz announcement.
- Passed teams, pre-registered teams and the first 15 waiting-list teams per class get the Hub setup email [Handbook 2.5].
- The quiz score also sets priorities such as team number and inspection order [Handbook 2.3.2, 4.2.3].
- Minimum score to pass: Not stated: check the quiz announcement.
- A question can be withdrawn after the quiz (975: "removed from the quiz") [FS Quiz 2026].

## Submission
- Open to teams with an active FSG 2026 Quiz account; no separate Formula IHU account [Handbook 2.2.1].
- One entry per team; if a team submits several times, only the first recorded counts [Handbook 2.3].
- Final: no edits and no resubmission [Handbook 2.3].
- No late entries after the 2-hour window [Handbook 2.2.1].
- Entered with the submission: team name, team email, class EV/CV, preferred and alternative team number (E## / C##), fuel type RON98 or E85 for CV [Handbook 2.2.1].
- The team email given here receives the Hub setup email [Handbook 2.5].
- How many members may answer, and whether outside help is allowed: Not stated: check the quiz announcement.
- Going back to earlier questions before submitting: Not stated: check the quiz announcement.
- Answer sheet shortly after the quiz; protests by 31-01-2026 to technical.formulaihu@ihu.gr, naming the question [Handbook 2.3.1].
- Results shortly after the protest period ends [Handbook 2.3.2].
- Dates above are for 2026; later dates: Not stated: check the quiz announcement.

## What they ask
Topic shares (own classification; all 32, then 2026 only):
- mechanics 7 (22%); 2026: 6 of 17 [FS Quiz 2024–2026]
- rules 6 (19%); 2026: 1 [FS Quiz 2024–2026]
- physics 6 (19%); 2026: 4 [FS Quiz 2024–2026]
- electronics 4 (13%); 2026: 3 [FS Quiz 2024–2026]
- other (trivia, puzzles) 4 (13%); 2026: 2 [FS Quiz 2024–2026]
- marketing/business 2 (6%); 2026: 0 [FS Quiz 2024–2026]
- math 1, dynamic-events 1, scoring 1 (3% each); 2026: scoring 1; static-events 0 [FS Quiz 2024–2026]

Recurring themes [FS Quiz 2024–2026]:
- FS Rules compliance and "which is true": 686, 688, 696
- Grey Areas safety-wire flex table used as data: 980, 982
- Formula IHU trivia feeding a calculation: 973 (Instagram hashtags), 974 (handbook release day 14)
- Greek and motorsport history trivia: 697, 699, 973
- Point-mass skidpad cornering with aero downforce: 695, 974
- Circuits: transformer, transistor stages, ADC, series termination: 698, 977, 978
- Materials and structures: gear steel, specific stiffness, sandwich panel, tensile test: 985, 986, 987
- CAD from a provided drawing: mass and a distance, then a changed-dimension follow-up: 988, 989
- Classical physics: heat exchanger, buoyancy, friction-damped spring: 689, 983, 981
- Business: break-even, ROI with currency conversion: 693, 694
- Dynamic events: track compliance, points with penalties: 691, 979
- Visual puzzles: roll centre, hidden watermark: 690, 976

Traps seen [FS Quiz 2024–2026]:
- The "trick" option is often right: "Not enough information" (691), "It's a trick question" (986), 0 cm³ above the oil when densities are equal (984).
- Chains carry errors forward: 984 needs 983's density, 986 needs 985's alloy, 989 needs 988's model.
- Irrelevant givens: 983's shape equation (only the floating fraction matters); 978's board thickness and I2C bus.
- 978: only each SPI line's driver gets a resistor (FPGA CLK, FPGA MOSI, MCU MISO); driver impedance = pull-up ∥ pull-down; R = 70 Ω − driver, nearest EIA-96 value (reproduces 66.5, 59, 61.9).
- Odd units: N/yard (981), kWh vs cal vs eV options (687), in² vs cm² vs mm² options (692), $ to € before ROI (694).
- The asked unit and the stored answer can disagree: 983 asks g/dm³ but stores 0.86 (that is g/cm³); note it for a protest [Handbook 2.3.1].
- Coolant in 983 is plain water, ρ = 1.0 g/cm³ [FS Rules T 7.2.1].
- Safety wire: 980 accepts 15 mm total flex on a 120 mm span (between table rows 101.6 mm / 12.7 mm and 127.0 mm / 15.9 mm); 982 uses the half-flex column (12.7 mm → 1.6 mm) [Grey Areas T 10.2.2].

## Event specifics
- The quiz runs on fihu.gr, not on the FSG site, but needs an FSG 2026 Quiz account [Handbook 2.2.1].
- Strong negative marking (−50% of the question's points) and tie-break on submission time [Handbook 2.3].
- Team number choice and CV fuel type go in the quiz submission [Handbook 2.2.1]; fuel type deadline 29-01-2026 23:59:59, the quiz day [Handbook 3.1].
- Pre-registered Greek and Cypriot teams still take the quiz [Handbook 2.3.3].
- EV teams must also take the FSG Quiz to register for FSG tools; CV teams need not [Handbook 3.2.1.1, 3.2.1.2].
- FS Rules 2026 V1.1 apply with FIHU additions [Handbook 1.3]; the Grey Areas Clarification supersedes FS Rules where applicable [Grey Areas intro].
- Handbook times are in CET; Athens uses EET/EEST; dates are DD-MM-YYYY [Handbook 2.2.1, 1.6.2].
- FIHU documents used as data: handbook release date 14-01-2026 [Handbook cover] in 974; Grey Areas T 10.2.2 in 980, 982 [FS Quiz 2026].
- FS Rules topics the questions cite: coolant T 7.2.1 (983), post-inspection penalties and dynamic scoring (979); 2024: steering wheel (685), ground clearance (686), impact attenuator energy (687), head restraint, locknuts, EDR (688), roll hoops (696) [FS Quiz 2024–2026].
- Local flavour: Greek politics (699), Formula IHU social media (973), "Formula Fihu" watermark (976) [FS Quiz 2024–2026].
