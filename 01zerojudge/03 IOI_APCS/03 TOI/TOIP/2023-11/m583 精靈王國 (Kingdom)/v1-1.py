# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m583. 精靈王國 (Kingdom)
# 2023-11 TOI 練習賽 新手組


k = int(input())
data = tuple(map(int, input().split()))
seen = [False] * k

result = 0
for i in range(k):
    if seen[i]:
        continue
    seen[i] = True
    cnt = 1
    i = data[i] - 1
    while seen[i] is False:
        seen[i] = True
        i = data[i] - 1
        cnt += 1
    result = max(result, cnt)

print(result)
