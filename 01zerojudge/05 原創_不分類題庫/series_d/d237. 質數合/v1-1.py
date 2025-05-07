# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d237. 質數合


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


if __name__ == '__main__':
    print(sum(eratosthenes(2 * 10 ** 6)))
