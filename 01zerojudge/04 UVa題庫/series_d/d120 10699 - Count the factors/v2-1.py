# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10699 Count the factors
# ZeroJudge d120


import math


def factorize(n: int) -> set:
    result = set()
    for i in (2, 3):
        if n % i == 0:
            result.add(i)
        while n > 1 and n % i == 0:
            n //= i

    for i in range(5, math.floor(math.sqrt(n)) + 1, 6):
        if n % i == 0:
            result.add(i)
        while n > 1 and n % i == 0:
            n //= i
        i += 2
        if n % i == 0:
            result.add(i)
        while n > 1 and n % i == 0:
            n //= i
    if n > 1:
        result.add(n)
    return result


def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(f'{n} : {len(factorize(n))}')


main()
