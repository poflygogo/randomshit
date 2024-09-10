from sys import stdin
from collections import Counter


for n in stdin:
    n = int(n)
    if not n:
        break
    data = Counter()
    for _ in range(n):
        stu = next(stdin).strip().split()
        stu.sort()
        data.update([int(''.join(stu))])
    data = tuple(data.values())
    result = max(data)
    print(result * data.count(result))
