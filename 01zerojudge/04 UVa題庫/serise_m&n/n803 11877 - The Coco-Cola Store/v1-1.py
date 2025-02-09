# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11877 The Coco-Cola Store
# ZeroJudge n803


def bottle(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return n // 3 + bottle(n % 3 + n // 3)


n = int(input())
while n:
    print(bottle(n))
    n = int(input())
