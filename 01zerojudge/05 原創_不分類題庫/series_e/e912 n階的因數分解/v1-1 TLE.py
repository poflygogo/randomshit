# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e912. n! 的因數分解


from sys import stdin

LIMIT = 10000


def eratosthenes(n: int = LIMIT) -> list:
    """質數篩法"""
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


prime = eratosthenes()
dp = [[0] * (len(prime) + 1) for _ in range(LIMIT + 1)]

print(len(prime))
exit()

# 質因數分解
for n in range(2, LIMIT + 1):
    m = n
    for p in range(len(prime)):
        while m % prime[p] == 0:
            dp[n][p] += 1
            m //= prime[p]
        if m == 1:
            break

# 二維前綴和
for i in range(2, LIMIT + 1):
    for j in range(len(prime)):
        dp[i][j] += dp[i - 1][j]


def string_formatter(s: list) -> str:
    """格式化字串"""
    return " * ".join(f"{prime[i]}^{s[i]}" for i in range(len(s)))


for n in stdin:
    n = int(n)
    result = dp[n][: dp[n].index(0)]
    print(f"{n}! = {string_formatter(result)}")
