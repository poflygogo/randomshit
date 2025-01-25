# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e795. p2.質數日
# 2019-12 TOI 新手同好會


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


def is_prime_day(date):
    div = 10000000
    while date > 0:
        if not is_prime(date):
            return False
        date %= div
        div //= 10
    return True


def main():
    for _ in range(int(input())):
        date = int(input())
        if is_prime_day(date):
            print(f'{date} is a Prime Day!')
        else:
            print(f'{date} isn\'t a Prime Day!')



if __name__ == '__main__':
    main()
