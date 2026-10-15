"""FSG 2023 quiz, problem 613: pressure after a pipe widening (Bernoulli).

Givens (question text; flow direction 1 -> 2 from figure 613_1):
    A1  = 2.55 cm^2   cross-section 1
    A2  = 7.1  cm^2   cross-section 2
    p1  = 1.2  bar    pressure in section 1
    v1  = 5    m/s    flow velocity in section 1
    rho = 997  kg/m^3 water
Pipe is horizontal (text), so no height term. Ideal, incompressible,
loss-free flow is assumed (nothing else is given).
Asked: p2 in bar, two decimals.
"""
from decimal import Decimal, ROUND_HALF_UP

CM2_TO_M2 = 1e-4
PA_PER_BAR = 1e5

area_1 = 2.55 * CM2_TO_M2      # m^2
area_2 = 7.1 * CM2_TO_M2       # m^2
pressure_1 = 1.2 * PA_PER_BAR  # Pa
velocity_1 = 5.0               # m/s
density = 997.0                # kg/m^3

# Continuity (incompressible): A1 v1 = A2 v2 -> the wider section is slower.
velocity_2 = velocity_1 * area_1 / area_2
print(f"v2 = {velocity_2:.6f} m/s")

# Bernoulli, horizontal: p1 + rho v1^2 / 2 = p2 + rho v2^2 / 2.
# The kinetic energy lost by slowing down reappears as static pressure.
pressure_2 = pressure_1 + 0.5 * density * (velocity_1**2 - velocity_2**2)
print(f"p2 = {pressure_2:.3f} Pa")

pressure_2_bar = pressure_2 / PA_PER_BAR
print(f"p2 = {pressure_2_bar:.6f} bar")
print(Decimal(repr(pressure_2_bar)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
