# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12459 Bees' ancestors
# ZeroJudge a519


dp = [0] * 81   # max input is 80
dp[1] = 1
dp[2] = 2
for i in range(3, 81):
    dp[i] = dp[i - 1] + dp[i - 2]

while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n])
