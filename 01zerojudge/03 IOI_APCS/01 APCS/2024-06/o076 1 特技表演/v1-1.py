# -*- encoding: utf-8 -*-
# python 3.12
# 2024-06 APCS
# ZeroJudge o076


n = int(input())
buildings = tuple(map(int, input().split()))

length = []
idx_start = 0
for i in range(1, n):
    if buildings[i] < buildings[i - 1]:
        continue
    length.append(i - idx_start)
    idx_start = i

if idx_start != n - 1:
    length.append(n - idx_start)

print(max(length))
