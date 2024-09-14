import math
import sys


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def sum_factors(n):
    factors = {}
    end = n * n
    for fac in factor:
        if fac > n: break
        while n % fac == 0:
            factors[fac] = factors.get(fac, 0) + 1
            n //= fac
    return sum([i * factors[i] for i in factors]) + (n if n != 1 else 0)


factor = eratosthenes(44721)
for num in sys.stdin:
    print(sum_factors(int(num)))
