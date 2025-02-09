# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00530 - Binomial Showdown
# ZeroJudge c061


from functools import reduce
from operator import mul


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    if m > n // 2:
        m = n - m
    print(reduce(mul, range(n - m + 1, n + 1)) // reduce(mul, range(1, m + 1)))
