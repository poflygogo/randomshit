# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b534. 質因數、最大公因數
# 102學年度商業類程式設計競賽


from math import gcd


def prime_factorize(n: int) -> dict:
    temp = {}
    p = prime_generator(n)
    i = next(p)
    while n >= i:
        if n % i == 0:
            temp[i] = temp.get(i, 0) + 1
            n //= i
        else:
            i = next(p)
    if n != 1:
        temp[n] = temp.get(n, 0) + 1
    return temp


def prime_generator(n):
    for i in (2, 3):
        yield i
    for i in range(5, n + 1, 6):
        yield i
        yield i + 2


for _ in range(int(input())):
    a, b = map(int, input().split())
    factors = prime_factorize(a)
    gcd_ab = gcd(a, b)

    print(
        '*'.join(f'{i}{"" if factors[i] == 1 else f"^{factors[i]}"}' for i in sorted(factors)),
        gcd_ab,
        'Y' if gcd_ab != 1 and gcd_ab in factors else 'N',
        sep=' , '
    )
