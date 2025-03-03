# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b112. 5. 高中運動會
# 


from functools import reduce
from math import gcd

while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(reduce(gcd, [int(input()) for _ in range(n)]))
