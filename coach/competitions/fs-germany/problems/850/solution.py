"""FSG 2024 quiz, problem 850: Fred vs Coco on the acceleration track.

Givens:
    track length 75 m from starting line to finish line
        (FS Rules D 5.1.1, quoted from FS-Rules_2026_v1.1.md; the question cites D 5.1.1)
    h  = 14 m        Coco's head start ahead of the start line (text, figure 850_2)
    v0 = 0 m/s       both start from rest at t = 0 s (text)
    a_Coco = 6 m/s^2 constant (text)
    Fred starts on the start line (figure 850_2); constant acceleration,
    no speed limit (text).
Asked: minimum acceleration of Fred in m/s^2 to reach the finish line at the
same time as Coco, one decimal.
"""
import math
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

TRACK_LENGTH = Fraction(75)       # m, D 5.1.1
HEAD_START = Fraction(14)         # m
COCO_ACCELERATION = Fraction(6)   # m/s^2

# From rest with constant a: s = a t^2 / 2  ->  t^2 = 2 s / a.
coco_distance = TRACK_LENGTH - HEAD_START
finish_time_squared = 2 * coco_distance / COCO_ACCELERATION
print(f"Coco covers {coco_distance} m in t = {math.sqrt(finish_time_squared):.6f} s")

# Fred must cover the full 75 m in that same time; a lower value arrives later.
fred_acceleration = 2 * TRACK_LENGTH / finish_time_squared
print(f"a_Fred = {fred_acceleration} m/s^2 = {float(fred_acceleration):.6f} m/s^2")

exact = Decimal(fred_acceleration.numerator) / Decimal(fred_acceleration.denominator)
# Half-up and rounding up both give the same one-decimal value here (7.377...).
print(exact.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
