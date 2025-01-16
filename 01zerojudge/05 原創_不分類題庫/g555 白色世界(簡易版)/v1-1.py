# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g555. 白色世界


dp = [0] * 200001   # 題目說最大的數字是 2e5
dp[1] = 1
for i in range(2, 200001):
    dp[i] = dp[i - 1] + dp[i - 2] + 1

for _ in range(int(input())):
    print(dp[int(input())])
