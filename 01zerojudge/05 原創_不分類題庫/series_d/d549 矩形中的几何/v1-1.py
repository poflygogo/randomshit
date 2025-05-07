# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d549. 矩形中的几何


import math


while True:
    try:
        a, b, c = map(int, input().split())
        print(f'{math.sqrt(a ** 2 - b ** 2 + c ** 2):.2f}')
    except EOFError:
        break
