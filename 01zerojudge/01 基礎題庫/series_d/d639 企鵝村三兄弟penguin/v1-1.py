# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d639. 企鵝村三兄弟penguin


LIMIT = 2781668
dp = [0] * (LIMIT + 1)
dp[0:4] = [1, 3, 5, 9]
for i in range(4, LIMIT + 1):
    dp[i] = sum(dp[i-3:i]) % 10007

n = int(input())
if n < 4:
    print(1)
else:
    print(dp[(n - 3) % LIMIT])
