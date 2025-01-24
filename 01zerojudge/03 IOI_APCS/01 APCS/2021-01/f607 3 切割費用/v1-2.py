# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f607. 3. 切割費用
# 2021-01 APCS


import bisect


N, L = map(int, input().split())
cut_trend = [tuple(map(int, input().split())) for _ in range(N)]
cut_trend.sort(key=lambda x: x[1])
line = [0, L]
cost = 0
for i, _ in cut_trend:
    idx = bisect.bisect_left(line, i)
    cost += line[idx] - line[idx - 1]
    line.insert(idx, i)
print(cost)
