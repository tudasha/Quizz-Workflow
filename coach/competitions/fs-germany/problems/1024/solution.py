"""FSG 2026, problem 1024: change of slalom time when the car is 0.05 m wider, with downforce.

Givens (question text; layout from images/1024_8.jpg):
    cones                  = 5, spacing L = 6 m, cone diameter d = 0.23 m
    safety distance        s = 0.3 m, cone edge to vehicle edge (figure: s between cone and cylinder)
    vehicle width          B = 1.3 m, change dB = +0.05 m
    aero effective length  aL = 1.6 m; aero area A = B x aL (simplification 3; "L" there is read
                           as the aerodynamic length aL: the 6 m cone spacing is not a car length,
                           and aL is otherwise unused)
    friction coefficient   mu = 1.22
    lift coefficient       cL = -2.1 (negative lift = downforce), constant for both widths
    mass                   m = 247 kg
Not given, assumed: air density rho = 1.225 kg/m^3 (ISA sea level), g = 9.81 m/s^2.
(rho 1.2 or 1.204 and g 9.80665 change the difference by < 0.0001 s; see notes.md.)

Geometry (figure): start and finish lie on the same side, level with the path apex at cone 1 and
cone 5; the path passes alternately beside cones 1..5 and is drawn smooth, apex to apex.
The car is a cylinder of diameter B, so its centre passes each cone at
    a = d/2 + s + B/2      (lateral offset of the path apex from the cone line).
Constant circular arcs (simplification 1): between two apexes the centre line is two equal arcs
of radius r, each centred on the vertical through a cone, meeting at the inflection point midway
(x = L/2, y = 0). The arc through the apex (0, a) with centre (0, a - r) reaching (L/2, 0):
    (L/2)^2 + (r - a)^2 = r^2  =>  r = ((L/2)^2 + a^2) / (2a)
    arc angle per half-arc: sin(theta) = (L/2) / r
4 apex-to-apex segments (cone 1 -> 5) x 2 half-arcs = 8 half-arcs: path = 8 r theta.

Speed (constant, simplification 1): grip limit with downforce,
    m v^2 / r = mu (m g + 0.5 rho |cL| A v^2)
    => v^2 = mu m g / (m / r - 0.5 mu rho |cL| A)
Time t = path / v; answer dt = t(B + dB) - t(B) in s (wider = positive dB; less time = negative).
"""
import math
from decimal import Decimal, ROUND_HALF_UP

CONE_SPACING_M = 6.0
CONE_COUNT = 5
CONE_DIAMETER_M = 0.23
SAFETY_DISTANCE_M = 0.3
WIDTH_REF_M = 1.3
WIDTH_DELTA_M = 0.05
AERO_LENGTH_M = 1.6
FRICTION_COEFF = 1.22
LIFT_COEFF = -2.1
MASS_KG = 247.0
AIR_DENSITY_KG_M3 = 1.225   # assumed, not given
GRAVITY_M_S2 = 9.81         # assumed, not given


def slalom_time(width_m):
    apex_offset_m = CONE_DIAMETER_M / 2 + SAFETY_DISTANCE_M + width_m / 2
    half_spacing_m = CONE_SPACING_M / 2
    radius_m = (half_spacing_m ** 2 + apex_offset_m ** 2) / (2 * apex_offset_m)
    half_arc_angle_rad = math.asin(half_spacing_m / radius_m)
    half_arc_count = 2 * (CONE_COUNT - 1)
    path_m = half_arc_count * radius_m * half_arc_angle_rad

    aero_area_m2 = width_m * AERO_LENGTH_M
    downforce_per_v2 = 0.5 * AIR_DENSITY_KG_M3 * abs(LIFT_COEFF) * aero_area_m2   # N/(m/s)^2
    speed_sq = FRICTION_COEFF * MASS_KG * GRAVITY_M_S2 / (MASS_KG / radius_m - FRICTION_COEFF * downforce_per_v2)
    speed_m_s = math.sqrt(speed_sq)
    return path_m / speed_m_s, path_m, radius_m, speed_m_s


time_ref, path_ref, radius_ref, speed_ref = slalom_time(WIDTH_REF_M)
time_new, path_new, radius_new, speed_new = slalom_time(WIDTH_REF_M + WIDTH_DELTA_M)
time_delta_s = time_new - time_ref

print(f"B = {WIDTH_REF_M:.2f} m: r = {radius_ref:.4f} m, path = {path_ref:.4f} m, v = {speed_ref:.4f} m/s, t = {time_ref:.5f} s")
print(f"B = {WIDTH_REF_M + WIDTH_DELTA_M:.2f} m: r = {radius_new:.4f} m, path = {path_new:.4f} m, v = {speed_new:.4f} m/s, t = {time_new:.5f} s")
print(f"dt = {time_delta_s:.6f} s")

print(Decimal(repr(time_delta_s)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
