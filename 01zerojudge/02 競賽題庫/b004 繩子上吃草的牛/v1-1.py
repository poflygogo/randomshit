# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b004. 繩子上吃草的牛
# 95學年度高雄市資訊學科能力競賽


from math import pi, sqrt

while True:
    try:
        D, L = map(int, input().split())
    except EOFError:
        break
    print(f'{(pi * L * sqrt(L ** 2 - D ** 2) / 4):.3f}')
