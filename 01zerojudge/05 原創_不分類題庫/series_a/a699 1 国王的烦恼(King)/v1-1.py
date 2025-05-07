# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a699. 1、国王的烦恼(King)


def mainloop():
    primes = eratosthenes(671065)
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        else:
            print(
                "It's a prime!!!" if n in primes else
                "It's not a prime!!!"
            )


def eratosthenes(n: int):
    primes = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return {p for p in range(2, n + 1) if primes[p]}


mainloop()
