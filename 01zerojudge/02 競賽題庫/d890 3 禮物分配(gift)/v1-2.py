# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d890. 3.禮物分配(gift)
# 99學年度台北市資訊學科能力競賽

# 0/1 背包

n, k = map(int, input().split())
gift = [int(input()) for _ in range(n)]

total = sum(gift)
total_half = total // 2

dp = [False] * (total_half + 1)
dp[0] = True

for price in gift:
    for j in range(total_half, price - 1, -1):
        dp[j] = dp[j] | dp[j - price]

for j in range(total_half, -1, -1):
    if dp[j]:
        result = j
        break

print(result, total - result)
