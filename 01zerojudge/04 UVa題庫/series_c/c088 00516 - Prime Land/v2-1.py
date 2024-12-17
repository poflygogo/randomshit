# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00516 Prime Land
# ZeroJudge c088


def main():
    primes = eratosthenes(32768)
    while True:
        factors = list(map(int, input().split()))
        if factors[0] == 0:
            break
        num = factors_to_int(factors)
        print(*int_to_factors(num - 1, primes))


def factors_to_int(factors: list) -> int:
    result = 1
    for i in range(0, len(factors), 2):
        result *= factors[i] ** factors[i + 1]
    return result


def int_to_factors(num: int, primes) -> list:
    factors = {}
    primes = iter(primes)
    p = next(primes)
    while num >= p:
        if num % p == 0:
            factors[p] = factors.get(p, 0) + 1
            num //= p
        else:
            p = next(primes)
    result = []
    for i in sorted(factors, reverse=True):
        result.extend([i, factors[i]])
    return result


def eratosthenes(n) -> list:
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


main()
