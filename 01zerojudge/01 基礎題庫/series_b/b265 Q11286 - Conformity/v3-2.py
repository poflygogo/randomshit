from sys import stdin
from collections import Counter


for n in stdin:
    n = int(n)
    if not n:
        break
    data = []
    for _ in range(n):
        stu = next(stdin).strip().split()
        stu.sort()
        data.append(int(''.join(stu)))
    data = Counter(data)
    data = tuple(data.values())
    result = max(data)
    print(result * data.count(result))
