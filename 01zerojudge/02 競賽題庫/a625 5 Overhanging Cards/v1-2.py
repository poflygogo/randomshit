# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a625. 5. Overhanging Cards
# HP CodeWars 2007


from fractions import Fraction as Frac
from itertools import accumulate
from bisect import bisect_left


harmonic_series = list(accumulate((Frac(1, i) for i in range(2, 274))))

while True:
    try:
        n = Frac(input())
    except EOFError:
        break
    else:
        print(bisect_left(harmonic_series, n) + 1, 'card(s)')
