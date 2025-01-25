# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e795. p2.質數日
# 2019-12 TOI 新手同好會


def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for p in  range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
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
