# Formula Student Germany — registration quiz

Pattern from the FS Quiz history (2016, 2018, 2020–2026, 111 questions, 4 with a written solution) and the 2026 handbook (FSG26_Event_Handbook_v1.1.md, DE 3.1). Written by Claude on 2026-10-14 ("Differs from FS Rules" on 2026-10-15); reviewed by: pending.

## When something is new
This file is the pattern of past quizzes and the 2026 handbook: a guide, not a rule.
- The question wins. If it asks for another type, unit, number of decimals or separator than this file says, follow the question and tell the member it differs from the usual pattern.
- Live quiz: when a question is of a kind this file does not cover (new type, new topic, new answer format, a scoring or submission detail not listed here), say so, solve it from the question and the current rules and handbook, and re-check your answer once more before giving it. Then log a note (`log-use`, `problem_id: note`) naming this competition and what was new, so a maintainer updates this file.
- Before a live quiz: check that `handbook/current/` is the newest handbook version and read the organiser's latest quiz announcement and FAQ. Where they differ from this file, they win; tell the member and log a note.
- When the weekly import brings a new handbook or new quiz questions for this competition, re-check this file against them.

## Differs from FS Rules 2026
Where this competition's 2026 handbook changes FS Rules 2026. For these points the handbook wins; check here before applying an FS Rules rule.
- **Points and formulas:** unchanged. The handbook runs the event under FS Rules 2026 and changes no discipline points or scoring formula, so FS Table 3 and D 9 apply as written [DE 1.3.1; FS A 1.2.5, D 9].
- **"No Driverless" status:** a team that sets it (cannot be undone) may not run in autonomous mode and scores 0 in every autonomous-mode discipline (EV class: DV Skidpad and DV Acceleration, 75 points each), instead of FS Table 3 listing them for every EV team [DE 3.5.1; FS A 1.2.5].
- **Endurance running order:** the next 5 cars must always queue; a car missing from it is out of order (2 min), allowed only at the end of its own session, never in or after the final one; a queue empty >5 min ends the session; FS leaves this to the handbook [DE 7.2.3–7.2.7; FS D 7.3.3, D 10.2.1].
- **Trackdrive running order:** the next 3 cars must always queue; a car missing from it is out of order with a 30 s penalty, allowed only at the end of Trackdrive; a queue empty >5 min ends Trackdrive, where FS has no Trackdrive out-of-order penalty [DE 7.3.2–7.3.6; FS D 8.2.3, D 10.2.1].
- **Session end (gong):** after the audio signal a run started before it may finish and re-runs are still granted, but no directly following second run, instead of FS's free option of a second run straight after the first [DE 7.1.2, DE 7.1.3; FS D 4.2.3, D 5.2.2, D 6.2.2].
- **Data logger download:** download each discipline's DL data at a DLDS within 1 h after it closes; late (team's fault) or EMI-corrupted data is a D 10.4.4 violation (DQ of the fastest valid run), where FS only says missing data is one [DE 8.3.3–8.3.5; FS D 10.4.2, D 10.4.4].
- **Track marking:** blue cones left, yellow right, small orange at entry/exit lanes, big orange at start, finish and timekeeping lines; max 5 m between cones unless chapter D says otherwise; no track limit lines for Acceleration and EBS Test; FS leaves this to the handbook [DE 7.5.1; FS D 2.4.1].
- **Cones and landmarks:** WEMAS cones with "FSG" on the band: big orange 285 × 285 × 505 mm, 1.05 kg; small 228 × 228 × 325 mm, 0.45 kg. Officials give no landmarks or map data, and teams must not add landmarks [DE 7.5.3–7.5.5; FS D 2.4.1].
- **Dynamic area:** trolleys, jacks and anything one member cannot carry by hand stay in the inspection and preparation areas, not in queues; during a run everyone but the ASR waits in a designated area, instead of FS's limit of what four members carry in one trip [DE 7.4.1, DE 7.4.2; FS D 1.4.5].
- **Supporting Material File:** at most 20 pages of content plus a title page and a table of contents page, where FS sets no page limit [DE 6.1.1; FS S 3.6].
- **Cost and Emissions Explanation File:** at most 20 pages of content, no more than 10 each for costs and for emissions, plus title, contents and an appendix of input values only (no calculations), where FS sets no page limit [DE 6.1.2; FS S 3.7].
- **No Tilt Test:** there is no Tilt Test at FSG 2026 and cars may drive the dynamic disciplines without it, but must still be able to pass it at any time (random checks), instead of having to pass every TI part, Tilt Test included, before driving [DE 5.15.1; FS IN 1.2.1, IN 7].
- **No CTMD:** no cell temperature monitoring device is installed at FSG 2026, so none is fitted at Accumulator Inspection or removed after Endurance, where FS lets the officials provide one that must be installed [DE 8.2.1; FS EV 5.8.9, IN 3.1.2, IN 12.1.10].
- **Electrical Inspection tools:** besides the IN 3.2.2 basic tools, bring an isolation-test device (IN 4.1.1), a milliohmmeter (EV 3.1.3), a voltage supply for the TS without its accumulator (IN 4.2.1) and, if applicable, a current source for the BSPD test [DE 5.14.1; FS IN 3.2.2, IN 4.2.1].
- **Accumulator delivery:** teams entering on Tuesday whose Accumulator Inspection is not that day must bring their accumulators to the charging area by 20:00; late costs 10 points per started 12 h, max 30, instead of FS's default of at least 20 points [DE 5.13.2, DE 5.13.3; FS A 3.8.1].
- **Sound limit:** every noise source on the car max 110 dB(C) at any time, measured from 0.5 m at any time during the event, so it applies to EVs too, instead of FS's 110 dB(C) limit for CV engines only (Noise Test is CV only) [DE 8.5; FS CV 3.2.1, IN 10].
- **RES:** must be the Gross-Funk GF2000i-codec/T53R98, latest 2022 revision with E-Key; its NO relay (max 4 A) is in the SDC; Node-ID 0x011; Race E-Key enabled by a flip switch marked "R" near the AMI, where FS leaves the model to the handbook [DE 8.4; FS T 14.3.1].
- **Data logger signals:** CAN 0x500 and 0x502 (always filled) and 0x501 (if sensors exist) every 100 ms; ASF signals in up to five messages 0x511–0x515 with a dbc file; little-endian, where FS leaves the basic signal set to the handbook [DE 8.3.8–8.3.13; FS T 14.2.2].
- **TI sticker space:** keep a space 50 mm tall × 180 mm wide on the nose directly in front of the cockpit opening, where FS only says the stickers go on the nose [DE 8.1.1; FS IN 1.3.1].
- **Charging area:** at most three members per team at a time, one of them an ESO, with no conductive jewellery or objects that could touch the accumulator, where FS sets no limit [DE 5.12.2, DE 5.12.3; FS A 6.12].
- **Document deadlines:** all in DE 4.2.1 Table 1 (BPEFS, TVSD, CRD, VSV, ESF and others); a file must be received before the deadline, so 13:00:00.000 is already late for 13:00; max 50 MB per document [DE 4.2.1–4.2.3; FS A 5.1.1, A 5.4.1].
- **No de-registration late in the season:** once the waiting list closes (2026-07-26 00:00 CEST), A 5.4.2 and A 5.3.4 are suspended, so late documents or incomplete corrections no longer de-register a team; A 5.4.1's 10 points are not suspended [DE 3.4.4; FS A 5.4.2, A 5.3.4].
- **Protests:** e-mail a request for clarification first, then after an informal review a formal e-mail protest within 2 h with the 25-point bond; deadlines fall between 10:00 and 22:00, at least 2 h after results (Endurance may be shorter), else 24 h after the incident [DE 5.4; FS A 3.7.2].
- **"No Driverless" documents:** no ASF, ASRQ or dbc file needed and no de-registration for missing them; open correction requests for them lapse, but penalties already incurred stay, instead of FS de-registering after 24 h [DE 3.5.2; FS A 5.4.2].
- **Classes:** only the EV class plus the Driverless Cup; no CV or HY class, instead of FS's CV (incl. HY) and EV classes [DE 1.2.1; FS A 1.2.1].
- **Driver registration:** at the egress tests; each driver shows a government driver's licence, national ID card and student ID, where FS asks only for the driver's licence [DE 5.9.1; FS A 4.2.10].

## Quiz format
- The quiz is the team registration; there is no registration without it [DE 3.1.1].
- Covers "all fields related to Formula Student" [DE 3.1.1].
- One question visible at a time [DE 3.1.6].
- One quiz for all teams: FSG 2026 has only the EV class, plus the Driverless Cup (DC) as an add-on [DE 1.2.1, DE 3.2.1]. All quizzes from 2020 to 2026 are listed as EV only; 2018 had an EV and a CV quiz with the same 16 questions [FS Quiz 2018–2026].
- Questions per quiz: 2016 12, 2018 16, 2020 9, 2021 11 + 11 (two quizzes, different questions), 2022 11, 2023 10, 2024 12, 2025 10, 2026 9 [FS Quiz 2016–2026].
- Types 2023–2026 (41 questions): input 21 (51%), multi-choice 15 (37%), single-choice 5 (12%) [FS Quiz 2023–2026].
- Trend: 2025 and 2026 had no single-choice questions. Every choice question is multi-choice, even with only one correct option (948, 1026, 1031). 2026 had 6 multi-choice and 3 input [FS Quiz 2025–2026].
- 28 of 41 recent questions come with images: figures, tables, datasheets [FS Quiz 2023–2026].
- Two questions were removed from the quiz afterwards: 841 for contradictory data, 949 with no reason given [FS Quiz 2024–2025].
- Open-book, internet, calculators, software, outside help: Not stated: check the quiz announcement.

## Time limit
- Each question has its own fixed duration; time is not shared across questions [DE 3.1.7]. Its weight, proportional to the duration, is shown with the question [DE 3.1.9].
- 2026 quiz start: 2026-01-30 13:00 CET [DE 4.1.1]. The quiz closes when the last question's time runs out [DE 3.1.11]. The official clock is formulastudent.de/time [DE 1.5.3].
- Total quiz length (sum of question times): 2026 62 min, 2025 71 min, 2024 79 min, 2023 87 min, 2022 101 min [FS Quiz 2022–2026].
- Per question, 2023–2026: 60–1200 s [FS Quiz 2023–2026].
- Input: 180–1200 s, median 600 s (n=21). Multi-choice: 120–600 s, median 300 s (n=15). Single-choice: 60–600 s, median 300 s (n=5) [FS Quiz 2023–2026].
- 900–1200 s goes to multi-step calculations (616, 849, 1024). 60–180 s goes to quick facts and one-step problems (851, 1030, 1023) [FS Quiz 2023–2026].
- Rule-statement checks with 10 options got only 120–300 s (848, 950, 1028), so rule lookup must be fast [FS Quiz 2024–2026].
- 2016 times are not recorded. In 2018 every recorded time was 300 s [FS Quiz 2016–2018].

## Decimals and answer format
- Each question sets its own rounding: "Round to one decimal", "with 2 decimal places", "nearest whole percent" [FS Quiz 2020–2026].
- Decimal places in input answers, 2023–2026 (31 values): 0 dp 13, 1 dp 4, 2 dp 11, 3 dp 3. All years (86 values): 0 dp 35, 1 dp 30, 2 dp 15, 3 dp 6 [FS Quiz 2016–2026].
- Answer keys keep trailing zeros up to the requested places: 45.0 (79), 0.70 (86), 1.590 (616), 0.00 (1029) [FS Quiz 2020–2026].
- Decimal separator: a dot. Questions convert the German comma explicitly: "if the screw core diameter is 12,3mm ... then use 12.3, 12" (158, 77, 159) [FS Quiz 2020–2021].
- Separator the platform accepts: Not stated: check the quiz announcement. The test site can be tried beforehand [DE 3.1.3].
- No units in input answers: a number only, in the unit the question names [FS Quiz 2016–2026].
- Percent is entered as a bare number: 12.34% → 12.34 (949, 620, 1030) [FS Quiz 2023–2026].
- Several values go in one field, separated by comma + space, in the order of the format line ("v1, v2, e.g. 1.2, 3.4") (75, 616). 1029 asked for six values [FS Quiz 2021–2026].
- Negative results take a leading minus (432 -2.0, 946 -10368, 1029 -40.84) [FS Quiz 2022–2026].
- A fully reduced fraction "numerator/denominator" when asked (67). Results "in multiples of P" are unitless (432) [FS Quiz 2021–2022].
- Rounding vs truncation: Not stated in the handbook.
- For "minimum", the FS Quiz solution rounds up: 88.68 → 88.69 (949). Discrete sizes are picked on the safe side (71, 617) [FS Quiz 2021–2025].
- When no rounding is stated, the keys were integers or had 2 decimals (667, 944) [FS Quiz 2018–2025].
- Multi-choice is asked as "Mark all correct answers" or "Select all that apply". Options are text, or letters A–D that refer to figures (1026, 852). There can be a "None of these are compliant" option (1025) [FS Quiz 2024–2026].

## Scoring
- There are no points. The rank comes from a total score, and a lower score ranks higher [DE 3.1.9].
- Per question: weight_i × time_team,i / (2 × time_question,i) for a valid answer, and weight_i × 1 for an invalid answer. The total is the sum over all questions [DE 3.1.9].
- A question's weight is proportional to its time limit and is shown with the question [DE 3.1.9].
- A valid answer scores 0 to 0.5 × weight, an invalid one 1 × weight. So a correct answer in the last second still beats any wrong answer: accuracy first, speed second [derived from DE 3.1.9].
- With weight = k × time limit, a valid answer costs k/2 per second on every question alike. A wrong answer costs as much as answering correctly for twice that question's time limit [derived from DE 3.1.9].
- A wrong answer costs the full weight and nothing more; there is no extra negative penalty [DE 3.1.9].
- Whether a missing answer counts as invalid: Not stated: check the quiz announcement.
- What "valid" means, and partial credit on multi-choice: Not stated: check the quiz announcement.
- Tie-breaks: Not stated: check the quiz announcement.
- Slots: 80 EV slots in total; up to 40 of these teams may also enter the DC [DE 3.2.1].
- Reserved slots go to past achievers: the 2025 crazy20 winner, the top 5 DC and top 5 EV teams of FSG 2025, the top 5 EV teams in the World Ranking List, and the 2025 WRL event winners [DE 3.2.2]. All other slots, including unused reserved ones, go by quiz rank [DE 3.1.15, DE 3.2.3].
- DC slots: 5 are reserved; the rest go by quiz rank [DE 3.6.2].
- Teams with a slot go to the pending list and must pay €1500 by PayPal within 72 h of the ranking's publication; everyone else goes to the waiting list [DE 3.1.16, DE 3.3.1, DE 3.3.3].
- The quiz rank also sets the Technical Inspection order, with DC teams first [DE 3.1.17, DE 5.10.2].
- No feedback on correctness until the results are published (2026-01-31 13:00 CET) [DE 3.1.12].
- Protests: within 4 h (until 17:00 CET), via the web form only; e-mail protests are ignored [DE 3.1.12].
- Times and ranking were published 2026-02-02 13:00 CET [DE 3.1.13].
- If protests show fundamental issues, the whole quiz is repeated (2026-02-06 13:00 CET) [DE 3.1.14].

## Submission
- Only one person answers: the team captain or one of their deputies [DE 3.1.4].
- The team account and team captain must exist 24 h before the start [DE 3.1.4].
- Each question can be answered only once, so an answer cannot be changed and there is no going back [DE 3.1.6].
- The answer must be given within the question's fixed time [DE 3.1.7].
- Late entry: depending on the delay, the first questions are no longer visible, so be logged in before the start [DE 3.1.8].
- Site: reg.formulastudent.de. A test site, t.reg.formulastudent.de, opens two weeks before (2026-01-16) [DE 3.1.3].
- After the quiz, the captain or a deputy registers the team: agree to the rules and pick a free vehicle number from 001 to 399. The number can be changed only within 168 h [DE 3.1.10].
- What counts as a submission (a typed but unsent answer when the time runs out, auto-submit): Not stated: check the quiz announcement.

## What they ask
- Topic shares by Claude's own classification of the question text, one primary topic per question; the `topic` field is empty for 2018 and 2022–2026.
- All years (111): rules/handbook 26%, electronics 23%, mechanics 18%, physics 17%, maths/CS/control 10%, business 5%, scoring 1% [FS Quiz 2016–2026].
- 2023–2026 (41): electronics 32%, rules/handbook 22%, maths/CS/control 17%, physics 15%, mechanics 10%, business 5% [FS Quiz 2023–2026].
- Rules/handbook share by year: 9 of 12 in 2016, then 0–3 per quiz since 2020; 3 per quiz in 2024–2026 [FS Quiz 2016–2026].

Recurring themes:
- Multi-statement checks on the FS Rules and the FSG handbook, with 8–10 options (848, 950, 1028)
- Statements on Business Plan Presentation (BPP) rules, asked as "which are false/INCORRECT" (943, 1023)
- Document deadlines, late penalties, de-registration (512, 452, 85)
- Trusses: zero-force members, then the support reactions (431/432, 618/619)
- Camera pixel plus distance → position in the vehicle frame, Euler angles ZY′X′′, reused with new numbers (434, 616)
- Circuits and RF: resistor networks, impedance, op-amp front ends, transfer functions, VSWR (942, 946, 1026, 1029)
- EV safety electrics: BSPD, picking a shutdown button from datasheets, TS fuse or circuit-breaker sizing, single point of failure (159, 617, 1025, 1031)
- Signals, digital logic and CS: sampling and aliasing, logic levels, IEEE 754 float32 (843, 844, 448, 1027)
- Kinematics and energy puzzles with Fred the racing alpaca or Coco the three-legged cat (620, 850, 615)
- Vehicle dynamics: traction and power limits, slalom, rollover (75, 1024, 515)
- Mechanics: gear trains, levers, bolt and tube sizing, thermodynamic cycles, fluids (612, 158, 613)
- Business and sustainability: NPV, make-or-buy, CO2e, storage time (72, 944, 941)

Traps seen:
- Singular wording "Which statement is CORRECT?" with 5–6 correct options (1027, 1028, 950); and multi-choice with only one correct option (948, 1026, 1031)
- Negated stems ("INCORRECT", "false"): select the false statements (943, 1023)
- A statement true under last year's rules is false now: a 2025 change removed a manual skidpad restriction (950 solution)
- "minimum" / "at least": round or step in the safe direction (949 solution, 71, 617)
- What looks like a long calculation can come out 0 by symmetry (447 → 0.0)
- The question sets the sign convention: "less time = negative" (1024), and negative reaction forces (432)
- float32 saturation: the result is 32768, not y × n (448)
- Mixed units within one answer (ms and s in 159); answers in kΩ (666, 842); min⁻¹ (612)
- Key data are only in the figure or a datasheet table (1025, 841, 944)

## Event specifics
- FS Rules 2026 contain nothing on the quiz; DE 3.1 is the only source [FS-Rules_2026_v1.1.md].
- Teams that only want the withdrawn list, to use FSG review tools for other events, must not take the quiz [DE 3.1.2].
- The score is weighted by time with no fixed points, and lower is better. This differs from per-question point systems [DE 3.1.9].
- 2026 changelog items: 80 EV slots and 40 DC slots (DE 3.2.1), extra Electrical Inspection tools including a milliohmmeter (DE 5.14.1), no tilt test (DE 5.15), no cell temperature monitoring device (DE 8.2) [Changelog, p. 2].
- 2026 quiz question 1028 tested two of these changelog items: 80 EV slots and the milliohmmeter [FS Quiz 2026].
- Rules the questions cite by number: D 4 skidpad (447), D 5.1.1 acceleration (850), EV 5.4.2/5.4.3 LVS in the TSAC (948), IN 11.2 EBS test (451), T 10.11 and A 5.4.2 (848) [FS Quiz 2022–2026].
- FSG handbook facts that were asked: slot counts (848, 1028), upload deadlines and the Hockenheim forklift (950), media photo credit (851), member pass requirements (435) [FS Quiz 2022–2026].
- Dates in options use YYYY-MM-DD hh:mm, CET/CEST (950) [DE 1.5.1, DE 1.5.2].
- The 2026 handbook dates are past. The FSG 2027 quiz date and rules: Not stated: check the quiz announcement.
