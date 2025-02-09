# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10789 Prime Frequency
# ZeroJudge a537


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


primes = set(eratosthenes(2000))
for cases in range(1, int(input()) + 1):
    text = input()
    counter = {}
    for i in text:
        counter[i] = counter.get(i, 0) + 1
    result = [i for i in counter if counter[i] in primes]
    result.sort()
    print(f'Case {cases}: {"".join(result) if result else "empty"}')
