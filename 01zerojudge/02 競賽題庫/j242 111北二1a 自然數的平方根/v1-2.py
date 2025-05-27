# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j242. 111北二1a.自然數的平方根
# 111北二區桃竹苗資訊學科能力複賽


from functools import reduce
from operator import mul


def main():
    n = int(input())
    factor = factorize(n)

    a = 1
    for i in factor:
        if factor[i] >= 2:
            a *= i ** (factor[i] // 2)
            factor[i] %= 2
    
    b = reduce(mul, [i ** j for i, j in factor.items()], 1)
    print('' if a == 1 else a,
          '' if b == 1 else f'sqrt({b})',
          sep=' ')


def factorize(n: int) -> dict:
    def div(k):
        nonlocal n
        while n % k == 0:
            result[k] = result.get(k, 0) + 1
            n //= k

    result = {}
    for i in (2, 3):
        div(i)
    for i in range(5, int(n ** 0.5) + 1, 6):
        div(i)
        div(i + 2)
    
    if n != 1:
        result[n] = 1
    return result


main()
