from sys import stdin
from collections import Counter


for case in stdin:
    n, m = map(int, case.strip().split())
    if n == m == 0: break

    data = Counter(next(stdin).strip() for _ in range(n * m - 1))
    print(min(data, key=lambda x: data[x]))
