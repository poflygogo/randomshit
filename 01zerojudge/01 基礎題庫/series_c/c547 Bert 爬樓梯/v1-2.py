# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c547. Bert 爬樓梯


dp = [0] * 10001
dp[1] = 1
dp[2] = 2
for i in range(3, 10001):
    dp[i] = dp[i - 1] + dp[i - 2]

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dp[n] % 1000000007)
