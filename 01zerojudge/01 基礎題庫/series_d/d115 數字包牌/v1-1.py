from sys import stdin
from itertools import combinations


for data in stdin:
    data = [int(i) for i in data.strip().split()]
    if data.pop(0) == 0: break

    chose = data.pop()
    data.sort()
    for i in combinations(data, chose):
        print(*i)
    print()
