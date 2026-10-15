"""FSG 2025, problem 946: DC steady-state output of a 7-stage analog input frontend.

Givens:
    Vin = 18 mV, R = 1 kOhm, 3R = 3 kOhm, C = 197 nF (question text)
    ideal op-amps (no bias current, no offset), ideal diode Vf = 0.6 V, no reverse leakage (text)
    circuit topology: images/946_4.jpg

Steady state with a DC input: every capacitor is an open circuit, so C does not matter.

Input polarity (figure): the voltage arrows follow the DIN/German convention, arrow from + to -.
The output arrow runs from the Vout terminal to ground, i.e. Vout = V(out) - V(ground), which
only reads naturally in that convention. The Vin arrow runs from the lower terminal to the upper
one, so the lower terminal is +Vin/2 and the upper one -Vin/2 (ground at the centre tap).

Stages, left to right (gains at DC):
 1  two non-inverting amps, R to ground, 3R||C feedback: gain 1 + 3R/R = 4 each
       V1_top = 4 * (-Vin/2), V1_bot = 4 * (+Vin/2)
 2  difference amp, top into "-", bottom into "+" (R in, 3R||C feedback / 3R||C to ground):
       V2 = 3 * (V1_bot - V1_top)
 3  top: C in series into "-", 3R feedback -> differentiator, DC output 0 (no current through C)
    bottom: non-inverting amp, gain 4:  V3_bot = 4 * V2
 4  difference amp, top into "-", bottom into "+", gain 3: V4 = 3 * (V3_bot - V3_top)
 5  inverting precision half-wave rectifier: R in, R||C feedback taken after the diode
    (anode at the op-amp output). It drives stage 6 through R into a virtual ground.
       V4 < 0 -> diode conducts, the loop is closed: V5 = -V4 (Vf is inside the loop)
       V4 > 0 -> op-amp swings negative, diode blocks: the node is then only fed through
                 R (input) + R (feedback) from V4 and loaded by R into the virtual ground of
                 stage 6, a 2R : R divider: V5 = V4 * R / (3R) = V4 / 3
 6  inverting amp, R in, 3R||C feedback: V6 = -3 * V5
 7  non-inverting amp, R to ground, 3R||C feedback taken after the series output R
    (no load, so no drop that matters): Vout = 4 * V6
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

VIN_MV = Fraction(18)          # mV, question
R_OHM = Fraction(1000)         # ohm, question (cancels in every gain)
R3_OHM = 3 * R_OHM
DIODE_VF_MV = Fraction(600)    # mV; inside the feedback loop when conducting, so it never appears

GAIN_NONINV = 1 + R3_OHM / R_OHM      # 4
GAIN_DIFF = R3_OHM / R_OHM            # 3

v_top_in = -VIN_MV / 2         # mV, DIN arrow convention (see docstring)
v_bot_in = +VIN_MV / 2

v1_top = GAIN_NONINV * v_top_in
v1_bot = GAIN_NONINV * v_bot_in
v2 = GAIN_DIFF * (v1_bot - v1_top)
v3_top = Fraction(0)                  # series capacitor blocks DC
v3_bot = GAIN_NONINV * v2
v4 = GAIN_DIFF * (v3_bot - v3_top)


def rectifier_stage(v_in_mv):
    """Stage 5 output node voltage, loaded by stage 6's input resistor R into a virtual ground."""
    if v_in_mv < 0:
        # diode forward biased: closed-loop inverting amp with gain -R/R
        return -v_in_mv
    # diode blocked: series path V4 -R- (op-amp "-") -R- node -R- 0 V (stage 6 virtual ground)
    return v_in_mv * R_OHM / (R_OHM + R_OHM + R_OHM)


v5 = rectifier_stage(v4)
v6 = -(R3_OHM / R_OHM) * v5
v_out_mv = GAIN_NONINV * v6

for label, value in [("V1 top", v1_top), ("V1 bottom", v1_bot), ("V2", v2), ("V3 top", v3_top),
                     ("V3 bottom", v3_bot), ("V4", v4), ("V5 (diode %s)" % ("on" if v4 < 0 else "off"), v5),
                     ("V6", v6), ("Vout", v_out_mv)]:
    print(f"{label:18s} {float(value):12.4f} mV")

answer = Decimal(v_out_mv.numerator) / Decimal(v_out_mv.denominator)
print(answer.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
