from fractions import Fraction
from sys import stdin


operate = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
for line in stdin:
    a1, a2, b1, b2, op = line.strip().split()
    print(
        operate[op](Fraction(int(a1), int(a2)),
                    Fraction(int(b1), int(b2))
                    )
    )

# python 3.12
