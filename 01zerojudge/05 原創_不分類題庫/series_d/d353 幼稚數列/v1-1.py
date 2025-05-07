# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d353. 幼稚數列

# look-and-say sequence 外觀數列
# 類似的題目: b541


import itertools


dp = [0] * 31
dp[0] = 1
for i in range(1, 31):
    dp[i] = int(''.join([f'{len(list(j))}{i}' for i, j in itertools.groupby(str(dp[i - 1]))]))

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(dp[n])
