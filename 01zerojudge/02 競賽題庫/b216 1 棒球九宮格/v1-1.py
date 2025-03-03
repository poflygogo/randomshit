# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b216. 1. 棒球九宮格
# 97學年度全國資訊學科能力競賽


flag = [[False] * 3 for _ in range(3)]
special = ((8, 5, 8),
           (5, 2, 5),
           (8, 5, 8))

for _ in range(9):
    x, y = map(int, input().split())
    if (x % 10 == 0) or (y % 10 == 0) or (not 0 < x < 30) or (not 0 < y < 30):
        continue
    flag[x // 10][y // 10] = True

lines = (sum(all(flag[i][j] for j in range(3)) for i in range(3)) +
         sum(all(flag[j][i] for j in range(3)) for i in range(3)))

score = sum(flag[i][j] * special[i][j] for i in range(3) for j in range(3))

print(lines, score)
