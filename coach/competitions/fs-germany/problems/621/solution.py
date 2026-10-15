"""FSG 2023 quiz, problem 621: ignition point in degrees crank angle before TDC.

Givens (question text; geometry from figure 621_1, in-line crank slider):
    s  = 52 mm   stroke, so crank radius r = s / 2 = 26 mm (figure: s = 2r)
    l  = 66 mm   connecting rod length (pin to pin)
    Sk = 2.0 mm  piston travel before TDC at ignition
    (d = 38 mm and the displacement 623.7 cm^3 are not needed for the angle;
     note 623.7 cm^3 does not match pi/4 d^2 s = 59.0 cm^3, so it is unused.)
Asked: crank angle before TDC in degrees, one decimal.
"""
import math
from decimal import Decimal, ROUND_HALF_UP

stroke = 52.0               # mm
rod_length = 66.0           # mm
ignition_travel = 2.0       # mm before TDC
crank_radius = stroke / 2   # mm

# At TDC the piston pin is r + l from the crank centre; Sk before TDC it is
# r + l - Sk. Crank radius, rod and that distance form a triangle, so the
# law of cosines gives the crank angle measured from TDC directly.
pin_distance = crank_radius + rod_length - ignition_travel
cos_crank_angle = (crank_radius**2 + pin_distance**2 - rod_length**2) / (
    2 * crank_radius * pin_distance
)
crank_angle = math.degrees(math.acos(cos_crank_angle))
print(f"crank-centre to piston-pin distance = {pin_distance} mm")
print(f"cos(phi) = {cos_crank_angle:.9f}")
print(f"phi = {crank_angle:.6f} deg before TDC")

# Verify with the slider-crank displacement formula: x = r(1 - cos phi) + l - sqrt(l^2 - r^2 sin^2 phi)
phi = math.radians(crank_angle)
travel = crank_radius * (1 - math.cos(phi)) + rod_length - math.sqrt(
    rod_length**2 - (crank_radius * math.sin(phi)) ** 2
)
print(f"check: piston travel at phi = {travel:.9f} mm")

print(Decimal(repr(crank_angle)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
