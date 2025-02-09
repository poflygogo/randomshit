# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10789 Prime Frequency
# ZeroJudge a537


def sieve():
    primes[1] = False
    primes[2] = True
    p = 3
    while p * p <= 2000:
        if primes[p]:
            for i in range(p * p, 2001, p << 1):
                primes[i] = False
        p += 2


primes = [i & 1 == 1 for i in range(2001)]
sieve()

for c in range(1, int(input()) + 1):
    counter = {}
    for i in input():
        counter[i] = counter.get(i, 0) + 1
    result = ''.join(i for i in sorted(counter) if primes[counter[i]])
    if not result:
        result = 'empty'
    print(f"Case {c}: {result}")
