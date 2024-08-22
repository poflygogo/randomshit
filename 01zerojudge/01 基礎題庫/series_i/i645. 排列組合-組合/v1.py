from sys import stdin
from itertools import combinations

for line in stdin:
    if line == "0 0\n": break

    a, b = map(int, line.split())
    items = [chr(i) for i in range(97, 97 + a)]

    result = combinations(items, b)

    for i in result:
        print(*i, sep='')