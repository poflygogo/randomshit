# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m605. 112北二5a.階乘計算 (Factorial)
# 112北二區桃竹苗資訊學科能力複賽


from itertools import groupby


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return {p:0 for p in range(2, n + 1) if primes[p]}


def prime_factorization(primes: dict, num: int):
    if num in primes:
        primes[num] += 1
        return
    for p in primes:
        while num % p == 0:
            primes[p] += 1
            num //= p
        if num == 1:
            return
        if num in primes:
            primes[num] += 1
            return

def format(arg):
    result = []
    for i, j in groupby(arg):
        j = len(list(j))
        if j == 1:
            result.append(str(i))
        else:
            result.append(f'{j}*{i}')
    return ' '.join(result)


def main():
    n = int(input())
    primes = eratosthenes(n)
    for i in range(2, n + 1):
        prime_factorization(primes, i)
    print(format(primes.values()))


if __name__ == '__main__':
    main()
