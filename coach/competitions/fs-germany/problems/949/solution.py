"""FSG 2025, problem 949: minimum reliability of "your component" for an 82 % Endurance finish.

Givens (question text):
    Endurance distance   = 22 km, 24 laps
    season goal          = 82 % probability to finish
    accumulator failure  ~ Normal(mu = 24.75 km, sigma = 1.7 km) in driven kilometres
    suspension failure   = 1 permille per lap, laps independent
    all failures independent; nothing else counts

Method:
    R_acc  = P(accumulator survives 22 km) = 1 - Phi((22 - mu) / sigma)
    R_susp = (1 - 0.001)^24
    independent series system: R_goal = R_acc * R_susp * R_comp
    => R_comp = R_goal / (R_acc * R_susp)
Phi via math.erf: Phi(z) = (1 + erf(z / sqrt(2))) / 2.
Rounding: the question asks for the MINIMUM reliability. Rounding half-up could land below
the true minimum and miss the 82 % goal, so the value is rounded up (ceiling) to 2 decimals,
the safe direction (COMPETITION.md: for "minimum", the FS Quiz solution rounds up).
"""
import math
from decimal import Decimal, ROUND_CEILING, ROUND_HALF_UP

ENDURANCE_KM = 22.0
LAPS = 24
GOAL_RELIABILITY = 0.82
ACC_MEAN_KM = 24.75
ACC_SIGMA_KM = 1.7
SUSP_FAILURE_PER_LAP = 0.001


def standard_normal_cdf(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


z_score = (ENDURANCE_KM - ACC_MEAN_KM) / ACC_SIGMA_KM
reliability_accumulator = 1.0 - standard_normal_cdf(z_score)
reliability_suspension = (1.0 - SUSP_FAILURE_PER_LAP) ** LAPS
reliability_component = GOAL_RELIABILITY / (reliability_accumulator * reliability_suspension)
component_percent = reliability_component * 100.0

print(f"z = {z_score:.6f}, R_acc = {reliability_accumulator:.8f}")
print(f"R_susp = {reliability_suspension:.8f}")
print(f"R_comp = {component_percent:.6f} %")
print(f"half-up would give {Decimal(repr(component_percent)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}; minimum -> round up")

print(Decimal(repr(component_percent)).quantize(Decimal("0.01"), rounding=ROUND_CEILING))
