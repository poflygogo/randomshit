# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n129. p1. 鋪磁磚問題
# 110新北市資訊學科能力複賽


n = int(input())
dp = [0] * n
dp[:3] = [1, 2, 4]

for i in range(3, n):
    dp[i] = sum(dp[i-3:i])

print(dp[n-1])
