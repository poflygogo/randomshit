# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00543 Goldbach's Conjecture   # zerojudge 題目編號有誤, 這題應該是 UVa 543
# ZeroJudge c050


import random


def is_prime(n, k=5):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

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


def goldbach(n):
    if is_prime(n - 3):
        return f'{n} = 3 + {n - 3}'
    for q in range(5, n // 2 + 1, 6):
        for p in (q, q + 2):
            if is_prime(p) and is_prime(n - p):
                return f'{n} = {p} + {n - p}'
    return 'Goldbach\'s conjecture is wrong.'


def main():
    while True:
        n = int(input())
        if not n:
            break
        result = goldbach(n)
        print(result)


if __name__ == '__main__':
    main()
