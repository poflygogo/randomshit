# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c634. 基礎排序 #2-1 ( 質因數和 ez)


from string import digits
from sys import stdin


def pattern(text):
    t = []
    n = []
    for i in text:
        if i in digits:
            n.append(i)
        else:
            t.append(i)
    t = ''.join(t)
    n = int(''.join(n))
    return -sum(factorize(primes, n)), t, -n


def factorize(primes, n):
    if n in primes:
        return [n]
    prime = iter(primes)
    p = next(prime)
    result = set()
    while n > 1:
        if n % p == 0:
            n //= p
            result.add(p)
        else:
            try:
                p = next(prime)
            except StopIteration:
                result.add(n)
                break
    return result


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


primes = eratosthenes(1000)
data = stdin.read().splitlines()
data.sort(key=pattern)
print('\n'.join(data))
