"""FSG 2025, problem 944: CO2e of ordering, storing, shipping and cutting a booster cushion.

Givens:
    pack ordered        = 2 cushions of 1000 mm x 1000 mm x 138 mm each (text: only packs of 2 sold)
    storage time        = 10 days in the warehouse (text)
    flight distance     = 15000 km (text)
    truck distance      = 450 km (text)
    cutting time        = 33 min, done twice: cut once, then "repeat the cutting process once" (text)
    density             = 40 kg/m^3 (table, images/944_3.jpg)
    warehouse factor    = 0.005 kgCO2e/h (table)
    flight factor       = 0.2 kgCO2e/(t*km) (table)
    truck factor        = 0.112 kgCO2e/(t*km) (table)
    workshop factor     = 0.05 kgCO2e/h (table)
The 350 x 350 x 138 mm target size only sets what is cut; it does not enter the CO2e.

Why: the transport factors are per tonne-kilometre, so the shipped mass is needed; the whole
pack of two cushions travels, so both count. Warehouse and workshop factors are per hour.
No rounding stated: 2 decimals (COMPETITION.md: unstated keys were integers or 2 decimals).
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

CUSHIONS_PER_PACK = 2
CUSHION_VOLUME_M3 = Fraction(1000, 1000) * Fraction(1000, 1000) * Fraction(138, 1000)  # m^3 each
DENSITY_KG_PER_M3 = Fraction(40)
STORAGE_HOURS = Fraction(10 * 24)                    # h, 10 days
FLIGHT_KM = Fraction(15000)
TRUCK_KM = Fraction(450)
CUT_MINUTES = Fraction(33)
CUT_COUNT = 2                                        # first cut + one repeat
WAREHOUSE_KG_PER_H = Fraction("0.005")
FLIGHT_KG_PER_T_KM = Fraction("0.2")
TRUCK_KG_PER_T_KM = Fraction("0.112")
WORKSHOP_KG_PER_H = Fraction("0.05")

shipped_mass_t = CUSHIONS_PER_PACK * CUSHION_VOLUME_M3 * DENSITY_KG_PER_M3 / 1000   # t
warehouse_kg = STORAGE_HOURS * WAREHOUSE_KG_PER_H
flight_kg = shipped_mass_t * FLIGHT_KM * FLIGHT_KG_PER_T_KM
truck_kg = shipped_mass_t * TRUCK_KM * TRUCK_KG_PER_T_KM
workshop_kg = CUT_COUNT * CUT_MINUTES / 60 * WORKSHOP_KG_PER_H
total_kg = warehouse_kg + flight_kg + truck_kg + workshop_kg

for label, value in [("shipped mass [t]", shipped_mass_t), ("warehouse", warehouse_kg),
                     ("flight", flight_kg), ("truck", truck_kg), ("workshop", workshop_kg),
                     ("total kgCO2e", total_kg)]:
    print(f"{label:18s} {float(value):.6f}")

answer = Decimal(total_kg.numerator) / Decimal(total_kg.denominator)
print(answer.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
