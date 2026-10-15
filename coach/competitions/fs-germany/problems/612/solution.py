"""FSG 2023 quiz, problem 612: output speed of a four-stage gear train.

Givens (all from the question text; the mesh order from figure 612_1):
    n1 = 3600 min^-1           input speed at sprocket z1 (motor)
    z1..z8 = 20, 45, 24, 55, 30, 43, 15, 53   teeth
    n2 = n3, n4 = n5, n6 = n7  pairs on a common shaft (text)
Meshes (figure): z1-z2, z3-z4, z5-z6, z7-z8, so z8 is driven through
three intermediate shafts.
Asked: n8 in min^-1, one decimal.
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

INPUT_SPEED = Fraction(3600)  # min^-1, text

TEETH = {1: 20, 2: 45, 3: 24, 4: 55, 5: 30, 6: 43, 7: 15, 8: 53}

# Each mesh (driver, driven): speed scales with z_driver / z_driven.
# Gears on a common shaft share the speed, so the stage ratios multiply.
MESHES = [(1, 2), (3, 4), (5, 6), (7, 8)]

speed = INPUT_SPEED
for driver, driven in MESHES:
    speed = speed * Fraction(TEETH[driver], TEETH[driven])
    print(f"n{driven} = {float(speed):.6f} min^-1")

total_ratio = INPUT_SPEED / speed
print(f"total ratio i = n1/n8 = {float(total_ratio):.6f}")

# Exact fraction kept until here; round once to one decimal, half up.
output_speed = Decimal(speed.numerator) / Decimal(speed.denominator)
print(output_speed.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
