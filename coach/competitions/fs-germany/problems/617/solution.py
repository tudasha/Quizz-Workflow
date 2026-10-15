"""FSG 2023 quiz, problem 617: size the TS circuit-breaker (rated current and breaking capability).

Givens (question text):
    V0    = 600 V DC        ideal source
    Ri    = 28.5 mOhm       all internal resistances of the TS energy storage
    breaker: instantaneous trip at 10 x In
    cable: 2 x 6 mm^2 (two conductors, TS+ and TS-), length l = 10 m
    kappa = 56 m/(Ohm mm^2) specific conductivity
    +30 % on the wire resistance for heating and other short-circuit effects
    In in steps of 10 A (choose the maximum that still trips instantly)
    Icn in steps of 10 kA (choose the minimum that still interrupts)
A short circuit between the two conductors at distance x from the storage
closes the loop out on one conductor and back on the other, so the wire
resistance in the loop is 2 x / (kappa A).
Asked: "In, Icn" with In in A and Icn in kA.
"""
import math
from decimal import Decimal

SOURCE_VOLTAGE = 600.0               # V
INTERNAL_RESISTANCE = 28.5e-3        # Ohm
TRIP_MULTIPLE = 10                   # instantaneous trip current / In
CONDUCTOR_AREA = 6.0                 # mm^2 per conductor
CABLE_LENGTH = 10.0                  # m
CONDUCTIVITY = 56.0                  # m / (Ohm mm^2)
SHORT_CIRCUIT_RESISTANCE_FACTOR = 1.3
RATED_CURRENT_STEP = 10              # A
BREAKING_CAPABILITY_STEP = 10        # kA

# Smallest fault current: short at the far end, the full loop (2 l) of wire
# in series, with the 30 % increase. It must still reach 10 x In.
loop_wire_resistance = (
    SHORT_CIRCUIT_RESISTANCE_FACTOR * 2 * CABLE_LENGTH / (CONDUCTIVITY * CONDUCTOR_AREA)
)
min_fault_current = SOURCE_VOLTAGE / (INTERNAL_RESISTANCE + loop_wire_resistance)
print(f"loop wire resistance (incl. +30 %) = {loop_wire_resistance * 1e3:.4f} mOhm")
print(f"minimum short-circuit current = {min_fault_current:.3f} A")

max_rated_current_exact = min_fault_current / TRIP_MULTIPLE
# Any higher step would trip later than instantaneous for a far-end fault,
# so step DOWN to the available size.
rated_current = math.floor(max_rated_current_exact / RATED_CURRENT_STEP) * RATED_CURRENT_STEP
print(f"In <= {max_rated_current_exact:.3f} A -> In = {rated_current} A")

# Largest fault current: short right at the start of the wire, only Ri limits it.
max_fault_current = SOURCE_VOLTAGE / INTERNAL_RESISTANCE
print(f"maximum short-circuit current = {max_fault_current:.3f} A")

# The breaker must interrupt it: step UP to the next available size.
breaking_capability = (
    math.ceil(max_fault_current / 1000 / BREAKING_CAPABILITY_STEP) * BREAKING_CAPABILITY_STEP
)
print(f"Icn >= {max_fault_current / 1000:.4f} kA -> Icn = {breaking_capability} kA")

print(f"{Decimal(rated_current)}, {Decimal(breaking_capability)}")
