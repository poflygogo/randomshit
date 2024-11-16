# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10170 The Hotel with Infinite Rooms
# ZeroJudge e555
# 
# 公式解


from math import ceil


while True:
    try:
        n, target = map(int, input().split())
    
    except EOFError:
        exit()
    
    else:
        print(ceil((-1 + ((1 - 4 * (-(n ** 2) + n - 2 * target))) ** 0.5) / 2))
