from itertools import combinations
from sys import stdin
from collections import Counter


_ = stdin.readline()
for _ in stdin:
    data = Counter([int(i) for i in stdin.readline().strip().split()])
    result = 0
    for a, b, c in combinations(sorted(data.keys()), 3):
        if a ** 2 + b ** 2 == c ** 2:
            result += data[a] * data[b] * data[c]
    print(result)
