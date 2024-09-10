from sys import stdin
from itertools import groupby


for n in stdin:
    n = int(n)
    if not n:
        break
    data = []
    for _ in range(n):
        stu = next(stdin).strip().split()
        stu.sort()
        data.append(''.join(stu))
    data.sort()
    data_group = groupby(data)
    data_group = [len(list(value)) for _, value in data_group]
    result = max(data_group)
    print(result * data_group.count(result))
