"""FSG 2025, problem 945: one-way transfer time of a 700 kB image.

Givens (question text):
    file size        = 700 kB      (SI prefix: 1 kB = 1000 byte, 1 byte = 8 bit)
    link rate        = 250 Mbit/s  (SI prefix: 1 Mbit = 10^6 bit, as data rates are quoted)
    round-trip delay = 60 ms
    stateless, no handshakes or encryption overhead; delay equal in both directions.

Method: one-way time = serialisation (transmission) time + one-way propagation delay.
    serialisation = bits / rate
    one-way delay = RTT / 2, because the delay is the same for download and upload
Answer in ms, nearest integer (question).
"""
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction

FILE_SIZE_BYTE = Fraction(700 * 1000)          # 700 kB
BITS_PER_BYTE = 8
LINK_RATE_BIT_PER_S = Fraction(250 * 10**6)    # 250 Mbit/s
ROUND_TRIP_S = Fraction(60, 1000)              # 60 ms

serialisation_s = FILE_SIZE_BYTE * BITS_PER_BYTE / LINK_RATE_BIT_PER_S
one_way_delay_s = ROUND_TRIP_S / 2
total_ms = (serialisation_s + one_way_delay_s) * 1000

print(f"serialisation = {float(serialisation_s) * 1000:.4f} ms, one-way delay = {float(one_way_delay_s) * 1000:.4f} ms")
print(f"total = {float(total_ms):.4f} ms")

answer = Decimal(total_ms.numerator) / Decimal(total_ms.denominator)
print(answer.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
