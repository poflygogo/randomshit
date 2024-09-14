from fractions import Fraction as Frac
from sys import stdin


def get_k(n: Frac) -> Frac:
    if n == 1:
        return n
    if n > 1:
        return get_k(n - 1) * 2
    else:
        return get_k(1 / n) + 1


for line in stdin:
    a, b = map(int, line.split())
    print(get_k(Frac(a, b)))
