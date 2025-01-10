# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10699 Count the factors
# ZeroJudge d120


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return tuple([p for p in range(2, n + 1) if primes[p]])


def factorize(n: int, prime: tuple) -> set:
    if n in set(prime):
        return {n}
    i = 0
    result = set()
    while i < len(prime) and n >= prime[i]:
        if n % prime[i] == 0:
            n //= prime[i]
            result.add(prime[i])
        else:
            i += 1
    if n > 1:
        result.add(n)
    return result


def main():
    prime = eratosthenes(1000)
    while True:
        n = int(input())
        if n == 0:
            break
        print(f'{n} : {len(factorize(n, prime))}')


main()
