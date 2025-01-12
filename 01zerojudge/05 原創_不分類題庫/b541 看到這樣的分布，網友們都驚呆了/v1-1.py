# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b541. 看到這樣的分布，網友們都驚呆了

# look-and-say sequence
# 類似的題目: d353

import itertools


dp = [0] * 41
dp[0] = 1
for i in range(1, 41):
    dp[i] = int(''.join([f'{len(list(j))}{i}' for i, j in itertools.groupby(str(dp[i - 1]))]))

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dp[n - 1])
