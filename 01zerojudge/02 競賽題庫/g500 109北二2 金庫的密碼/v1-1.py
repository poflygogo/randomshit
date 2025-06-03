# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g500. 109北二2.金庫的密碼
# 109北二區桃竹苗資訊學科能力複賽


from itertools import combinations

n = int(input())

possible = 0
for a, b, c, d, e in combinations(range(1, 31), 5):
    if (a * 20 + b ** 2 + c * 3 + (c + d) * 4 + (e - d) * 5) == n:
        possible += 1

if possible:
    print(possible ** 3)
else:
    print(n * 5 - 3)
