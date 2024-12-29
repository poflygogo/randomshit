# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c547. Bert 爬樓梯


dp = [0, 1, 2]
while True:
    try:
        n = int(input())
    except EOFError:
        break

    while len(dp) - 1 < n:
        dp.append(dp[-1] + dp[-2])
    
    print(dp[n] % 1000000007)
