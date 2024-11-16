# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00482 Permutation Arrays
# ZeroJudge e529


for _ in range(int(input())):
    input()

    p = tuple(map(int, input().split()))
    x = input().split()

    print(*sorted(x, key=lambda i: p[x.index(i)]), sep='\n')
