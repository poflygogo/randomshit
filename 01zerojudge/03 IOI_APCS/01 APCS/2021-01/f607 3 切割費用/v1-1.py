# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f607. 3. 切割費用
# 2021-01 APCS


def binary_search(item):
    lft, rgt = 0, len(line)
    while lft < rgt:
        mid = (lft + rgt) // 2
        if line[mid] < item:
            lft = mid + 1
        else:
            rgt = mid
    return lft


N, L = map(int, input().split())
cut_trend = [tuple(map(int, input().split())) for _ in range(N)]
cut_trend.sort(key=lambda x: x[1])
line = [0, L]
cost = 0
for i, _ in cut_trend:
    idx = binary_search(i)
    cost += line[idx] - line[idx - 1]
    line.insert(idx, i)
print(cost)
