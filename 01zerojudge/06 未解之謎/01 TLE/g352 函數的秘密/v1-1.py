# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g352. 函數的秘密
# 改編自 Atcoder Regular Contest 127 A


digit = int(input())
limit = int(input())

result = 0
for i in range(digit, 0, -1):
    for j in range(i, 0, -1):
        t = int('1' * j + '0' * (i - j))
        if t <= limit:
            result += min(limit - t + 1, 10 ** (i - j))
            result %= 998244353

print(result)


# 思路:
# https://ikatakos.com/pot/programming_algorithm/contest_history/atcoder/2021/0925_arc127
