# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c666. 質數乘積


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


primes = eratosthenes(49000)[:5000]
primes_mul = [primes[0]] + [0] * 4999
for i in range(1, 5000):
    primes_mul[i] = primes_mul[i - 1] * primes[i]

while True:
    try:
        n = int(input())
    except:
        break
    else:
        print(primes_mul[n - 1])
