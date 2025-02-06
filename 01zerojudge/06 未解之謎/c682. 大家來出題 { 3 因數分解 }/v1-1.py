# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c682. 大家來出題 { 3: 因數分解 }


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(n // 10, n + 1) if primes[p]]


w, v = map(int, input().split())
primes = eratosthenes(10 ** v)
i = 0
n = iter(range(i + 1, len(primes)))
for _ in range(w):
    j = next(n)
    if j == len(primes) - 1:
        i += 1
        n = iter(range(i + 1, len(primes)))
    print(primes[i] * primes[j], primes[i], primes[j])
