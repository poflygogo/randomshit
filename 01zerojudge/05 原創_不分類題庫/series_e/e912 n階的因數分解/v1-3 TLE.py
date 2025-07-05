# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e912. n! 的因數分解


from sys import stdin
from math import sqrt, floor
from collections import Counter

LIMIT = 10000


def eratosthenes(n: int) -> list:
    """質數篩法"""
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


prime = eratosthenes(floor(sqrt(LIMIT)))
data = [Counter({2:1})]
for n in range(3, LIMIT + 1):
    temp = data[-1].copy()
    for p in prime:
        while n % p == 0:
            temp[p] = temp.get(p, 0) + 1
            n //= p
        if n < p:
            break
    if n != 1:
        temp[n] = 1
        prime.append(n)
    data.append(temp)


def formatter(t: dict):
    return " * ".join(f"{i}^{j}" for i, j in t.items())


for n in stdin:
    n = int(n)
    print(f"{n}! = {formatter(data[int(n) - 2])}")
