# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c547. Bert 爬樓梯


mod = 1000000007
dp = [0] * 10001
dp[1] = 1
dp[2] = 2
for i in range(3, 10001):
    dp[i] = (dp[i - 1] % mod + dp[i - 2] % mod) % mod

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dp[n])
