# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e795. p2.質數日
# 2019-12 TOI 新手同好會


def eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return {p for p in range(2, n + 1) if primes[p]}


def is_prime_day(primes, date):
    div = 10000000
    while date > 0:
        if date not in primes:
            return False
        date %= div
        div //= 10
    return True


def main():
    primes = eratosthenes(29991232)
    for _ in range(int(input())):
        date = int(input())
        if is_prime_day(primes, date):
            print(f'{date} is a Prime Day!')
        else:
            print(f'{date} isn\'t a Prime Day!')



if __name__ == '__main__':
    main()
