# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f580. 2. 骰子
# 2020-07 APCS


n, m = map(int, input().split())
dice = [[1, 4, 2] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    if b > 0:
        dice[a], dice[b - 1] = dice[b - 1], dice[a]
    elif b == -1:
        dice[a][0], dice[a][1] =  7 - dice[a][1], dice[a][0]
    elif b == -2:
        dice[a][0], dice[a][2] = 7 - dice[a][2], dice[a][0]

print(*[i[0] for i in dice])
