# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k849. P3.骨牌 (Domino)
# 2021-10 TOI 新手同好會


data = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    data[b] = a

result = [-1]
while result[-1] in data:
    result.append(data[result[-1]])
result.pop(0)

print(*reversed(result))
