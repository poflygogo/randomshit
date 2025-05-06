# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a702. Cousin Primes


# ---------------------------------------------------

import sys
import io
Q = """1
2
3
4
18888"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



import random


def is_prime(n, k=3):
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


def main():
    from sys import stdin

    LIMIT = 20000000
    cousin_primes = [(3, 7)]
    cousin_primes.extend([(i, i + 4) for i in range(7, LIMIT + 1, 6) if is_prime(i) and is_prime(i + 4)])
    result = [cousin_primes[int(i) - 1] for i in stdin.readlines()]
    print('\n'.join(f'({i[0]}, {i[1]})' for i in result))


main()
