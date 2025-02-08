# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00568 Just the Facts
# ZeroJudge c055


from sys import stdin


dp = [0] * (int(1e4) + 1)
dp[1] = 1
for i in range(2, int(1e4) + 1):
    temp = i * dp[i - 1]
    while temp % 10 == 0:
        temp //= 10
    dp[i] = temp % 100000   # mod 取到 1e5 就可以，因為數字最大只到 1e6

for n in stdin:
    n = int(n)
    print(f'{n:>5d} -> {dp[n] % 10}')
