# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o077. 2. 電子畫布
# 2024-06 APCS


h, w, n = map(int, input().split())
canvas = [[0] * w for _ in range(h)]

for _ in range(n):
    r, c, t, x = map(int, input().split())
    up = r - t if r - t >= 0 else 0
    down = r + t + 1 if r + t + 1 <= h else h
    lft = c - t if c - t >= 0 else 0
    rgt = c + t + 1 if c + t + 1 <= w else w
    for i in range(up, down):
        for j in range(lft, rgt):
            if abs(i - r) + abs(j - c) <= t:
                canvas[i][j] += x

print('\n'.join(' '.join(str(i) for i in row) for row in canvas))
