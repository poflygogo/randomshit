# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e932. pB. 數字拆解
# 2014大學學測推甄申請二階


n = int(input())

# dp[i][j] 表示將 i 拆解成最大值不超過 j 的方法數
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0] = [1] * (n + 1)   # n=0 時，無論 max_val 是多少，都只有一種拆解方式 (空集)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 情況一：不使用 j (最大值為 j-1)
        dp[i][j] = dp[i][j - 1]

        # 情況二：使用 j (所以 n 變成 i-j，最大值仍為 j)
        # 確保 i-j 不會是負數
        if i - j >= 0:
            dp[i][j] += dp[i - j][j]

print(dp[n][n])
