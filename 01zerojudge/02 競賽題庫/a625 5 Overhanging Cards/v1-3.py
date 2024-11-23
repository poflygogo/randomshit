# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a625. 5. Overhanging Cards
# HP CodeWars 2007


from bisect import bisect_left


harmonic_series = [0.5]
for i in range(3, 274):
    harmonic_series.append(harmonic_series[-1] + 1 / i)

while True:
    try:
        n = float(input())
    except EOFError:
        break
    else:
        print(bisect_left(harmonic_series, n) + 1, 'card(s)')
