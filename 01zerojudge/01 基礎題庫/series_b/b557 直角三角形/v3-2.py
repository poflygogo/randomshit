from itertools import combinations
from sys import stdin


_ = stdin.readline()
for _ in stdin:
    data = {}
    for i in stdin.readline().strip().split():
        i = int(i)
        data[i] = data.get(i, 0) + 1
    result = sum(
        [data[a] * data[b] * data[c]
         for a, b, c in combinations(sorted(data.keys()), 3)
         if a ** 2 + b ** 2 == c ** 2
         ]
    )
    print(result)
