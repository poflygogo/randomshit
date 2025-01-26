# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e811. 3. 密碼產生器 (Password)
# 2019-11 TOI 練習賽 潛力組


P, Q, R, a0, a1, N = map(int, input().split())

dp = [0] * (N + 1)
dp[:2] = [a0, a1]
for i in range(2, N + 1):
    dp[i] = (P * dp[i - 1] + Q * dp[i - 2] + R) % 10000

print(str(dp[-1]).zfill(4))
