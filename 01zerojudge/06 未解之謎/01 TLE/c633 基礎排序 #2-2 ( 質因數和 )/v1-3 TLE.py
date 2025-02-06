# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c633. 基礎排序 #2-2 ( 質因數和 )


from string import digits
from sys import stdin
import random


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
    if n in primes or (n > primes[-1] and is_prime(n)):
        return [n]
    prime_iter = iter(primes)
    p = next(prime_iter)
    result = set()
    while n > 1:
        if n % p == 0:
            n //= p
            result.add(p)
        elif p == primes[-1]:
            result.add(n)
            break
        else:
            p = next(prime_iter)
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


def is_prime(n, k=5):
    # Miller-Rabin
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s = s >> 1

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


primes = eratosthenes(1000)
data = stdin.read().splitlines()
data.sort(key=pattern)
print('\n'.join(data))
