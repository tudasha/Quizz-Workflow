# Key values: FS Rules 2026

The numbers quiz questions use most, from FS Rules 2026 v1.1 (`current/FS-Rules_2026_v1.1.md`). Each line ends with the rule and a short quote from it.
- Read the rule in context before you answer, and cite the rule, not this file.
- **2026** marks a rule the FS Rules changelog lists as changed for 2026 (`current/FS-Rules_2026_v1.1.changes.md`). A past problem from an earlier year may use the old value.
- A competition's handbook can change a value: check the section Differs from FS Rules in its `COMPETITION.md` first.
- CI checks that every quote is still in the rules, so a new rules version shows what to update.

## Points
- Maximum points, CV and EV: BPP 75, Cost and Manufacturing 100, Engineering Design 150, Skidpad 50, DV Skidpad 75, Acceleration 50, DV Acceleration 75, Autocross 100, Endurance 250, Efficiency 75; total 1000 [A 1.2.5, table 3: "Endurance 250 points -"]
- Maximum points, Driverless Cup: Engineering Design 150, DV Skidpad 75, DV Acceleration 75, DV Autocross 100, Trackdrive 200; total 600 [table 3: "Overall 1000 points 600 points"]
- A team needs at least one valid run in a dynamic discipline to score points in it [D 1.1.9: "a team must have at least one valid run in that"]

## Dynamic scoring
The formulas are garbled in the .md; they are written out here from the PDF (pages 131 to 133).
- Skidpad, Acceleration, Autocross, Endurance (**2026**): SCORE = (Pmax − Pmin) · ((Tmax − Tteam) / (Tmax − Tmin))² + Pmin. Tteam is the team's best time including penalties, capped at Tmax; Tmin is the fastest vehicle's time including penalties [D 9.1.1: "Tteam is the team’s best time including penalties. Tteam is capped to Tmax."]
- Tmax and Pmin (**2026**) [D 9.1.1, table 11]:
  - Skidpad: Tmax = 1.35 Tmin, Pmin = 0.05 Pmax ["Skidpad 1.35 Tmin 0.05 Pmax"]
  - Acceleration: 1.7 Tmin, 0.05 Pmax ["Acceleration 1.7 Tmin 0.05 Pmax"]
  - Autocross: 1.4 Tmin, 0.1 Pmax ["Autocross 1.4 Tmin 0.1 Pmax"]
  - Endurance: 1.5 Tmin, 0.1 Pmax ["Endurance 1.5 Tmin 0.1 Pmax"]
  - Driverless Cup Skidpad: 1.7 Tmin, 0.05 Pmax ["[DC ONLY] Skidpad 1.7 Tmin 0.05 Pmax"]
  - Driverless Cup Acceleration: 2.25 Tmin, 0.05 Pmax ["[DC ONLY] Acceleration 2.25 Tmin 0.05 Pmax"]
- DV Skidpad and DV Acceleration: DV_SCORE = Pmax · (Nall + 1 − RDV,team) / Nall. RDV,team is the rank of the team's best autonomous time including penalties; Nall is the number of teams with at least one valid manual or autonomous run. A run over 25 s without penalties is disqualified [D 9.2: "Runs with a run time without penalties >25 s will be disqualified."]
- Driverless Cup Autocross: 0.9 Pmax · (Tmax − Tteam,total) / (Tmax − Tmin) + 0.1 Pmax, with Tteam,total = min(Tteam,1, avg(Tteam,1, Tteam,2)). Tmax is the lap time at 6 m/s; DNF, DQ and slower runs count as Tmax [D 9.3.2: "Tmax is the time for driving the lap with 6 m/s."]
- Trackdrive: 0.75 Pmax · (Tmax / Tteam − 1), Tteam capped at Tmax, Tmax = 2 × the fastest corrected elapsed time; plus 2.5 % of Pmax for every completed lap [D 9.3.3, D 9.3.4: "Tmax is 2 times of the corrected elapsed time of the fastest vehicle."]
- Efficiency (**2026**): Pmax · ((EFmax − EFteam) / (EFmax − EFmin))², EFmax = 2 · EFmin, EF = T² · E. T is the uncorrected elapsed driving time; E is the corrected fuel mass (CV) or the used energy (EV) [D 9.4: "EFmax is defined as 2· EFmin"]
- EV used energy: regenerated energy × 0.9 is subtracted [D 7.9.5: "Regenerated energy is multiplied by 0.9 and subtracted from the used energy."]

## Penalties
Table in D 10.1.7, columns Acceleration, Skidpad, Autocross, Endurance, Trackdrive.
- Cone down or out (DOO): 2 s; Skidpad 0.2 s ["DOO 2 s 0.2 s 2 s 2 s 2 s"]
- Off course (OC): DQ in Acceleration and Skidpad; 10 s in Autocross, Endurance and Trackdrive ["OC DQ DQ 10 s 10 s 10 s"]
- Unsafe stop (USS): DQ in Acceleration, Skidpad and Autocross; not used in Endurance; −50 points in Trackdrive ["USS DQ DQ DQ n/a"]
- Not obeying a flag: 1 min [D 10.1.8: "Failure to obey a flag: 1 min time penalty."]
- Vehicle-to-vehicle contact: 2 min up to DQ [D 10.1.10: "Vehicle to vehicle contact: 2 min up to DQ"]
- Not starting within 30 s of the green flag: DQ for that run [D 10.1.11: "the vehicle is DQ for that run."]
- Endurance out of order: 2 min [D 10.2.1: "are penalized by 2 min"]
- Endurance too slow: average over two consecutive laps below 8 m/s dry or 5 m/s wet, may be disqualified [D 10.2.4: "below 8 m/s in dry conditions or below 5 m/s in wet or damp conditions"]
- Driver change procedure broken: up to 2 min [D 10.2.5: "will lead to a time penalty of up to 2 min"]
- EV power, current or voltage over the limit (moving average over 500 ms): the fastest valid run of that discipline is disqualified, one run per violation; missing data logger data counts as a violation (**2026**) [D 10.4: "Non-availability of data logger data will be treated as a violation."]

## Dynamic disciplines
- Drivers: 3 to 4 per team; a driver drives in at most 2 dynamic disciplines and at most 2 runs in each; at most 2 drivers per discipline; Endurance and Efficiency count as one discipline [D 1.2: "a minimum of three and a maximum of four drivers"]
- Acceleration: 75 m from starting line to finish line [D 5.1.1: "with a length of 75 m from starting line to finish line"]
- Skidpad: circle centres 18.25 m apart, inner circles 15.25 m and outer circles 21.25 m in diameter [D 4.1.2: "The centers of these circles are 18.25 m apart."]
- Autocross: one lap, under 1.5 km; straights at most 80 m; slalom cones 7.5 m to 12 m apart [D 6.1, D 6.2.1: "The length of the Autocross track is less than 1.5 km."]
- Endurance: about 22 km, laps about 1 km; 3 min for the driver change, extra time counts [D 7.1, D 7.5.4: "The length of the complete Endurance is approximately 22 km."]
- Trackdrive (Driverless Cup): 10 laps of about 200 m to 500 m [D 8.1.2, D 8.3.1: "A run consists of ten laps."]

## EV electrical
- Power: at most 80 kW at the TSAC outlet [EV 2.2.1: "The TS power at the outlet of the TSAC must not exceed 80 kW."]
- Current (**2026**): at most 500 A at the TSAC outlet, also when regenerating [EV 2.2.2, EV 2.2.3: "The TS current at the outlet of the TSAC must not exceed 500 A."]
- Voltage: at most 600 V DC between any two points; 630 V DC for motor controller and AMS internal low power control signals [EV 4.1.1: "600 VDC and for motor controller and AMS internal low power control signals 630 VDC."]
- Low voltage system: at most 60 V DC or 50 V AC RMS [T 11.1.2: "LVS is 60 VDC or 50 VACRMS."]
- Shutdown: when the SDC opens, the TS voltage must drop below 60 V DC and 50 V AC RMS in less than 5 s; opening the AIRs may be delayed by at most 250 ms [EV 6.1.5: "the voltage in the TS must drop to below 60 VDC and 50 VACRMS in less than"]
- Pre-charge: to at least 95 % of the actual accumulator voltage before the second AIR closes [EV 5.7.1: "least 95 % of the actual TS accumulator voltage before closing the second AIR"]
- TSAL: red light flashing at 2 Hz to 5 Hz with a 50 % duty cycle [EV 4.10.2: "The TSAL itself must have a red light, flashing continuously with a frequency between 2 Hz"]
- TSAC indicator: a red LED is lit above 60 V DC or half the maximum TS voltage, whichever is lower, on the vehicle side of the AIRs [EV 5.4.8: "full brightness whenever a voltage greater than 60 VDC or half the maximum TS voltage,"]
- IMD: response value at least 500 Ω/V of the maximum TS voltage; tested at 250 Ω/V, must shut down the TS within 30 s [EV 6.3.3, IN 4.1.2: "The response value of the IMD must be set to≥500 Ω/V"]
- Accumulator segment: at most 120 V DC, 6 MJ and 12 kg [EV 5.3.2: "maximum energy of 6 MJ, see EV 5.1.2, and a maximum mass of 12 kg."]
- BSPD: opens the SDC on hard braking while at least 5 kW goes to the motors (EV) or the throttle is more than 25 % over idle (CV), when it lasts more than 500 ms; brake pressure threshold at most 30 bar [T 11.6: "the brake pressure is≤30 bar."]
- Shutdown buttons: at least 40 mm diameter on the sides, 24 mm in the cockpit; the charger's emergency stop at least 24 mm [T 11.4.3, T 11.4.4, EV 7.1.6: "buttons on both sides of the vehicle is 40 mm."]

## Vehicle and inspection
- Wheelbase: at least 1525 mm [T 2.9.1: "The vehicle must have a wheelbase of at least 1525 mm."]
- Tilt Test: 60°, with the tallest driver strapped in and all fluids full; no leaks and all wheels stay on the table [IN 7.1: "The vehicle will be placed upon the tilt table and to an angle of 60"]
- CV noise: 110 dB(C) up to the test speed (average piston speed 15.25 m/s, rounded to the nearest 500 rpm), 103 dB(C) at idle, fast weighting [CV 3.2: "corresponds to an average piston speed of 15.25 m/s."]
