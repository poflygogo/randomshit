# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p905. 找數字 (Numbers)
# TOI 練習賽 新手組


from math import sqrt, cbrt, floor


def is_prime(n: int):
    if n == 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, floor(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def find_next_prime(n: int):
    t = (1, 4, 3, 2, 1, 2)  # make number 6n + 1 or 6n - 1
    n += t[n % 6]
    while not is_prime(n):
        n += t[n % 6]
    return n


def find_next_square(n: int):
    return (floor(sqrt(n)) + 1) ** 2


def find_next_cube(n: int):
    return (floor(cbrt(n)) + 1) ** 3


def main():
    ans = []
    n = int(input())
    ans.append(find_next_prime(n))
    ans.append(find_next_square(n))
    ans.append(find_next_cube(n))
    print(*ans)


if __name__ == '__main__':
    main()
