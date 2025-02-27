# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11342 - Three-square
# ZeroJudge d188


from math import sqrt, floor


def three_square(n):
    n_sqrt = floor(sqrt(n)) + 1
    for i in range(n_sqrt):
        i_sqr = i * i
        for j in range(i, floor(sqrt(n - i_sqr)) + 1):
            j_sqr = j * j
            k = sqrt(n - i_sqr - j_sqr)
            if k.is_integer():
                return i, j, floor(k)
    return -1,


for _ in range(int(input())):
    print(' '.join(map(str, three_square(int(input())))))
