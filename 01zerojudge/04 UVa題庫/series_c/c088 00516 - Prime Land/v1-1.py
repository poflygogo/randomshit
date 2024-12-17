# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00516 Prime Land
# ZeroJudge c088


def main():
    while True:
        factors = list(map(int, input().split()))
        if factors[0] == 0:
            break
        num = factors_to_int(factors)
        print(*int_to_factors(num - 1))


def factors_to_int(factors: list) -> int:
    result = 1
    for i in range(0, len(factors), 2):
        result *= factors[i] ** factors[i + 1]
    return result


def int_to_factors(num: int) -> list:
    factors = {}
    primes = prime_generator(num)
    p = next(primes)
    while num >= p:
        if num % p == 0:
            factors[p] = factors.get(p, 0) + 1
            num //= p
        else:
            p = next(primes)
    result = []
    for i in sorted(factors, reverse=True):
        result.extend([i, factors[i]])
    return result
    

def prime_generator(maxint: int):
    """「質數」生成器，跳過那些明顯不可能為質數的數字"""
    for i in (2, 3):
        yield i
    for i in range(5, maxint + 1, 6):
        yield i
        yield i + 2


main()
