# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g501. 109北二4.旅遊的規劃
# 109北二區桃竹苗資訊學科能力複賽


from itertools import combinations

data = [{1, 2, 3, 5, 6, 8, 11, 13, 17, 21, 22}, 
        {2, 3, 5, 7, 8, 13, 16, 17, 21, 22, 24},
        {1, 3, 5, 6, 7, 15, 16, 17, 22, 23, 24, 25},
        {2, 4, 5, 7, 8, 15, 17, 21, 23, 25}]

h = int(input())
n = int(input())

popular_spot = {i for i in range(1, 26) if sum(i in j for j in data) >= h}

result = 0
for i in combinations(popular_spot, n):
    i = set(i)
    if sum(i.issubset(j) for j in data) >= h:
        result += 1

print(result)
