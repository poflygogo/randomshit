# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f313. 2. 人口遷移
# 2020-10 APCS


from copy import deepcopy


row, col, k, m = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(row)]

for _ in range(m):
    temp = deepcopy(cities)
    for r in range(row):
        for c in range(col):
            if temp[r][c] == -1:
                continue
            change = cities[r][c] // k
            cnt = 0
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if not (0 <= i < row) or not (0 <= j < col) or cities[i][j] == -1:
                    continue
                temp[i][j] += change
                cnt += 1
            temp[r][c] -= change * cnt
    cities = temp


# find the maximum and the minimum value
max_value, min_value = float('-inf'), float('inf')
for r in range(row):
    for c in range(col):
        if cities[r][c] == -1:
            continue
        max_value = max(max_value, cities[r][c])
        min_value = min(min_value, cities[r][c])

print(min_value, max_value, sep='\n')
