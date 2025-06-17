# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d890. 3.禮物分配(gift)
# 99學年度台北市資訊學科能力競賽

# 0/1 背包

n, k = map(int, input().split())
gift = [int(input()) for _ in range(n)]

total = sum(gift)
total_half = total // 2

# dp[i][j] -> 表示考慮前 i 件禮物時，是否能湊出總價值為 j 
dp = [[False] * (total_half + 1) for _ in range(n + 1)]  
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(total_half + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= dp[i - 1][j]:
            dp[i][j] = dp[i][j] | dp[i - 1][j - gift[i - 1]]
    
for j in range(total_half, -1, -1):
    if dp[n][j]:
        result1 = j
        break

print(result1, total - result1)
