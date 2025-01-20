# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f513. 舉旗遊戲 (Flag)
# 2020-12 TOI 練習賽 新手組


row, col = map(int, input().split())
data = [input().split() for _ in range(row)]

cnt = 0
for r in range(row):
    for c in range(col):
        if all(
            data[i][j] != data[r][c]
            for i in range(r - (r > 0), r + 1 + (r < row - 1))
            for j in range(c - (c > 0), c + 1 + (c < col - 1))
            if (i, j) != (r, c)
            ):
            cnt += 1

print(cnt)
