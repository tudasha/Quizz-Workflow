"""FSG 2025, problem 942: total resistance of the resistor network in the figure.

Topology read from images/942_2.jpg (node names are mine):
    T1  = upper-left terminal, wired straight to node A
    A   = upper-left junction
    B   = top-middle junction (between 100 ohm and 180 ohm on the top rail)
    C   = bottom-middle junction (between 390 ohm and 180 ohm on the lower rail)
    D   = right-hand vertical wire; it joins the ends of both 180 ohm resistors
          and the right end of the 150 ohm resistor, so it is one node
    T2  = lower-left terminal, reaches D through the 150 ohm resistor

Branches (ohm), all from the figure:
    A-B : 100            (top rail)
    A-C : 100 + 390      (vertical 100 ohm down from A, then 390 ohm along the lower rail: in series)
    B-C : 220            (vertical bridge resistor)
    B-D : 180            (top rail, right)
    C-D : 180            (lower rail, right)
    D-T2: 150            (bottom wire)

A-B-C-D is an unbalanced bridge (100/180 != 490/180), so no series/parallel shortcut:
solve it by nodal analysis with exact fractions, then add the 150 ohm in series.
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

R_AB = Fraction(100)            # ohm, figure
R_AC = Fraction(100 + 390)      # ohm, figure: 100 ohm vertical + 390 ohm in series
R_BC = Fraction(220)            # ohm, figure
R_BD = Fraction(180)            # ohm, figure
R_CD = Fraction(180)            # ohm, figure
R_SERIES = Fraction(150)        # ohm, figure: between D and the lower terminal

# Inject 1 A into A, take D as 0 V. Unknowns V_A, V_B, V_C; KCL at each node.
# The resistance between A and D is then V_A / 1 A.
g_ab, g_ac, g_bc, g_bd, g_cd = (1 / r for r in (R_AB, R_AC, R_BC, R_BD, R_CD))
conductance_matrix = [
    [g_ab + g_ac, -g_ab, -g_ac],
    [-g_ab, g_ab + g_bc + g_bd, -g_bc],
    [-g_ac, -g_bc, g_ac + g_bc + g_cd],
]
current_vector = [Fraction(1), Fraction(0), Fraction(0)]


def solve_linear(matrix, rhs):
    """Gauss-Jordan elimination on Fractions (exact, no pivoting problems here)."""
    size = len(rhs)
    augmented = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(size):
        pivot_row = next(r for r in range(col, size) if augmented[r][col] != 0)
        augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]
        pivot = augmented[col][col]
        augmented[col] = [value / pivot for value in augmented[col]]
        for r in range(size):
            if r != col and augmented[r][col] != 0:
                factor = augmented[r][col]
                augmented[r] = [a - factor * b for a, b in zip(augmented[r], augmented[col])]
    return [augmented[r][size] for r in range(size)]


v_a, v_b, v_c = solve_linear(conductance_matrix, current_vector)
r_bridge = v_a                      # ohm, A to D
r_total = r_bridge + R_SERIES       # ohm, terminal to terminal

print(f"R_bridge (A-D) = {r_bridge} = {float(r_bridge):.6f} ohm")
print(f"R_total        = {r_total} = {float(r_total):.6f} ohm")

# Question: "in Ohm, round to the nearest one"
answer = Decimal(r_total.numerator) / Decimal(r_total.denominator)
print(answer.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
