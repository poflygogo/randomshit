# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d887. 1.山脈種類(chain)
# 99學年度台北市資訊學科能力競賽


LIMIT = 25
dp = [[0] * (LIMIT + 1) for _ in range(LIMIT + 1)]

for i in range(1, LIMIT + 1):
    for j in range(1, LIMIT + 1):
        if i == 1:
            dp[i][j] = 1
        elif i > j:
            dp[i][j] += dp[i - 1][j]
        else:
            dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dp[n][n])
