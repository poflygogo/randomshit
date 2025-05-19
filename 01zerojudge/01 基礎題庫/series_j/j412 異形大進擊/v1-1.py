# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j412. 異形大進擊


max_row, max_col, holes = map(int, input().split())
holes_info = {tuple(map(int, input().split())) for _ in range(holes)}

dp = [[0] * (max_col + 1) for _ in range(max_row + 1)]
dp[1][1] = dp[0][2 % max_col] = dp[2 % max_row][0] = 1

for row in range(1, max_row + 1):
    for col in range(1, max_col + 1):
        if (row, col) not in holes_info:
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        else:
            dp[row][col] = 0

print(dp[-1][-1])
