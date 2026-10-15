"""FSG 2024 quiz, problem 842: impedance across the body diagonal of an RLC cube.

Givens (question text):
    R = 4.7 kOhm (3x), C = 470 nF (6x), L = 4.7 uH (3x)
    sinusoidal source 12 V, f = 50 Hz (the 12 V does not change an impedance)
Topology (figure 842_1, a cube; input = front bottom-left corner,
output = back top-right corner, the opposite corner):
    the 3 edges at the input corner are the resistors,
    the 3 edges at the output corner are the inductors,
    the 6 remaining "middle" edges are the capacitors.
By the threefold symmetry about the input-output diagonal, the three corners
next to the input share one potential and the three corners next to the output
share another. So the cube is three groups in series:
    3 R in parallel  +  6 C in parallel  +  3 L in parallel.
Asked: |Z| in kOhm, two decimals.
"""
import cmath
import math
from decimal import Decimal, ROUND_HALF_UP

RESISTANCE = 4.7e3      # Ohm
CAPACITANCE = 470e-9    # F
INDUCTANCE = 4.7e-6     # H
FREQUENCY = 50.0        # Hz

omega = 2 * math.pi * FREQUENCY
z_resistor = complex(RESISTANCE, 0)
z_capacitor = 1 / (1j * omega * CAPACITANCE)
z_inductor = 1j * omega * INDUCTANCE

# Equipotential corner groups: no current flows between corners of one group,
# so identical edges between two groups act in parallel.
z_total = z_resistor / 3 + z_capacitor / 6 + z_inductor / 3
print(f"Z_C (one capacitor) = {z_capacitor.imag:.4f}j Ohm")
print(f"Z_L (one inductor)  = {z_inductor.imag:.6f}j Ohm")
print(f"Z = {z_total.real:.4f} {z_total.imag:+.4f}j Ohm")

magnitude_kohm = abs(z_total) / 1e3
print(f"|Z| = {magnitude_kohm:.6f} kOhm, phase = {math.degrees(cmath.phase(z_total)):.3f} deg")
print(Decimal(repr(magnitude_kohm)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
