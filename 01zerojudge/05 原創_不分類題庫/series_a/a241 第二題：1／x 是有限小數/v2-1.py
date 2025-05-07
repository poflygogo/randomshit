# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a241. 第二題：1 / x 是有限小數


import math


def mainloop():
    for _ in range(int(input())):
        n = int(input())


def calc(n: int) -> int:
    a = math.log(n, 2)
    b = math.log(n, 5)
    c = math.log(n, 10)
    
    a, b, c = map(math.floor, (a, b, c))
    return a // c + a // c

print(calc(10 ** 8))

