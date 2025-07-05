# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00160 Factors and Factorials
# ZeroJudge d131


from sys import stdin


def eratosthenes(n: int = 100) -> list:
    """質數篩法"""
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def string_formatter(s: list, flag: bool = False) -> str:
    """格式化字串(這題的格式寫起來真麻煩)"""
    if flag:
        return (
            string_formatter(s[:15])
            + "\n"
            + " " * 6
            + string_formatter(s[15:])
        )
    else:
        return "".join(map(lambda x: str(x).rjust(3), s))


prime = eratosthenes()
dp = [[0] * (len(prime) + 1) for _ in range(101)]

# 質因數分解
for n in range(2, 101):
    m = n
    for p in range(len(prime)):
        while m % prime[p] == 0:
            dp[n][p] += 1
            m //= prime[p]
        if m == 1:
            break

# 二維前綴和
for i in range(2, 101):
    for j in range(len(prime)):
        dp[i][j] += dp[i - 1][j]

for n in stdin:
    n = int(n)
    if n == 0:
        break
    result = dp[n][: dp[n].index(0)]
    print(f"{n:>3d}! ={string_formatter(result, len(result) > 15)}")
