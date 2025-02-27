# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11342 - Three-square
# ZeroJudge d188


from math import sqrt, floor


def three_square(n):
    n_sqrt = floor(sqrt(n)) + 1
    for i in range(n_sqrt):
        for j in range(i, floor(sqrt(n - sqr[i])) + 1):
            k = sqrt(n - sqr[i] - sqr[j])
            if k.is_integer():
                return i, j, floor(k)
    return -1,


sqr = [i ** 2 for i in range(floor(sqrt(50000)))]
for _ in range(int(input())):
    print(' '.join(map(str, three_square(int(input())))))
