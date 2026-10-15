"""FSG 2026, problem 1030: share of the power delivered to the antenna that is transmitted.

Given (question text):
    VSWR = 6.47 (6.47:1), measured with a vector network analyser.

Method: the reflection coefficient magnitude follows from the VSWR,
|Gamma| = (VSWR - 1) / (VSWR + 1). The reflected power share is |Gamma|^2,
so the transmitted (accepted) share is 1 - |Gamma|^2 (mismatch loss; the antenna's
radiation efficiency is not given, so it is taken as the accepted power).
Answer in percent, nearest whole percent (question).
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

VSWR = Fraction("6.47")                       # dimensionless, question text

gamma_magnitude = (VSWR - 1) / (VSWR + 1)     # dimensionless
reflected_share = gamma_magnitude ** 2
transmitted_share = 1 - reflected_share
transmitted_percent = transmitted_share * 100

print(f"|Gamma| = {float(gamma_magnitude):.6f}")
print(f"reflected = {float(reflected_share) * 100:.4f} %, transmitted = {float(transmitted_percent):.4f} %")

answer = Decimal(transmitted_percent.numerator) / Decimal(transmitted_percent.denominator)
print(answer.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
