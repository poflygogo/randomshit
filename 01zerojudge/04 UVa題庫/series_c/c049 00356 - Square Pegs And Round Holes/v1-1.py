# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00356 Square Pegs And Round Holes
# ZeroJudge c049


from sys import stdin
import math


is_not_first_case = False
for n in stdin:
    n = int(n.rstrip())
    height = r = (2 * n - 1) / 2  # 半徑, 圓上一點與圓直徑的垂線長度
    rr = r ** 2                   # 經常重複用到的數字先存起來
    inter = contain = 0           # 在圓內的格子, 在圓上的格子
    for x in range(1, math.ceil(r)):
        y = math.sqrt(rr - x ** 2)
        inter += 2 * (math.ceil(height) - math.ceil(y) + 1)
        contain += math.floor(y) * 2
        height = y

    inter += math.ceil(height) * 2
    inter *= 2
    contain *= 2

    print(
        ('\n' if is_not_first_case else '') +
        f'In the case n = {n}, {inter} cells contain segments of the circle.',
        f'There are {contain} cells completely contained in the circle.',
        sep='\n',
        )
    is_not_first_case = True
