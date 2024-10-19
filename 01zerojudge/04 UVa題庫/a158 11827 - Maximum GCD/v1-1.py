from math import gcd
from itertools import combinations


for _ in range(int(input())):
    print(max(map(lambda x: gcd(*x), combinations(map(int, input().split()), 2))))


# python 3.6.9
# zerojudge a158
# UVa 11827
# AC (0.2s, 3.4MB)
# 2024-10-19
