"""FSG 2024 quiz, problem 849: railgun charge voltage to hit the basket.

Givens (question text; layout from figure 849_1):
    l     = 1 m          rail (accelerator) length; its lower end is at the origin
    alpha = 77.25 deg    tilt above horizontal
    m     = 0.567 kg     cannonball
    C     = 33 mF        total capacitance
    g     = 980.665 cm/s^2 = 9.80665 m/s^2
    basket at (4.191 m, 3.05 m)
    no friction, no energy loss (capacitor energy fully goes into the ball)
Model: the ball starts at rest at the origin, is accelerated along the rail
and leaves at the rail's top end (l cos alpha, l sin alpha) with speed v at
angle alpha, then flies on a drag-free parabola through the basket.
Energy balance over the rail: C U^2 / 2 = m v^2 / 2 + m g l sin(alpha)
(the ball is also lifted l sin(alpha) while it is accelerated).
Asked: charge voltage U in V, rounded to the nearest one.
"""
import math
from decimal import Decimal, ROUND_HALF_UP

rail_length = 1.0                     # m
launch_angle = math.radians(77.25)    # rad
ball_mass = 0.567                     # kg
capacitance = 33e-3                   # F
gravity = 980.665e-2                  # m/s^2 (given in cm/s^2)
basket_x, basket_y = 4.191, 3.05      # m

# Muzzle (end of rail) position: the flight starts here, not at the origin.
muzzle_x = rail_length * math.cos(launch_angle)
muzzle_y = rail_length * math.sin(launch_angle)
dx = basket_x - muzzle_x
dy = basket_y - muzzle_y
print(f"muzzle at ({muzzle_x:.6f}, {muzzle_y:.6f}) m")

# Projectile path from the muzzle: dy = dx tan(a) - g dx^2 / (2 v^2 cos^2 a),
# solved for the launch speed v.
speed_squared = gravity * dx**2 / (
    2 * math.cos(launch_angle) ** 2 * (dx * math.tan(launch_angle) - dy)
)
muzzle_speed = math.sqrt(speed_squared)
print(f"muzzle speed v = {muzzle_speed:.6f} m/s")

kinetic_energy = 0.5 * ball_mass * speed_squared
potential_energy = ball_mass * gravity * muzzle_y  # lift along the rail
required_energy = kinetic_energy + potential_energy
print(f"E_kin = {kinetic_energy:.6f} J, E_pot (rail lift) = {potential_energy:.6f} J")
print(f"capacitor energy needed = {required_energy:.6f} J")

# E = C U^2 / 2
charge_voltage = math.sqrt(2 * required_energy / capacitance)
print(f"U = {charge_voltage:.6f} V")
print(Decimal(repr(charge_voltage)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
