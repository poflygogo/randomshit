# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11204 Musical instruments
# ZeroJudge j064


from functools import reduce
from operator import mul

for _ in range(int(input())):
    total_instrument, total_student = map(int, input().split())
    favorite = {}
    for _ in range(total_student):
        # 我們只在乎學生最喜歡的樂器
        t = input().split().index('1')
        favorite[t] = favorite.get(t, 0) + 1
    print(reduce(mul, favorite.values(), 1))
