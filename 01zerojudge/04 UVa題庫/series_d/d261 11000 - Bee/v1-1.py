# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11000 Bee
# ZeroJudge d261


# [male bee, female bee]
dp = [[0, 0] for _ in range(50)]
dp[0] = [0, 1]
for i in range(1, 50):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0] + 1

while True:
    n = int(input())
    if n == -1:
        break
    print(dp[n][0], sum(dp[n]))
