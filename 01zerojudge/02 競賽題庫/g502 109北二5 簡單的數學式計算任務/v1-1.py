# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g502. 109北二5.簡單的數學式計算任務
# 109北二區桃竹苗資訊學科能力複賽


from functools import reduce
from operator import mul

expr = input().split('+')
result = sum(reduce(mul, map(int, i.split('*')), 1) for i in expr)
print(result % 100_000)
