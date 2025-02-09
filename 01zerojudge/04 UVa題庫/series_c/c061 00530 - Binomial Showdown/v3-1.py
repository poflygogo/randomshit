# -*- encoding: utf-8 -*-
# python 3.6.9
# UVa 00530 - Binomial Showdown
# ZeroJudge c061


from functools import reduce


def comb_for_reduce(a, b):
    return a * (n - m + b) // b


n, m = map(int, input().split())
while not n == m == 0:
    m = min(m, n - m)
    print(reduce(comb_for_reduce, range(1, m + 1), 1))
    n, m = map(int, input().split())
