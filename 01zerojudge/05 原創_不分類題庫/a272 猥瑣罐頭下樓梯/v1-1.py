# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a272. 猥瑣罐頭下樓梯


LIMIT = 20016
dp = [0] * (LIMIT + 1)
dp[1] = 1
dp[2] = 2

for i in range(3, LIMIT + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

while True:
    try:
        print(dp[int(input()) % LIMIT])
    except EOFError:
        break
