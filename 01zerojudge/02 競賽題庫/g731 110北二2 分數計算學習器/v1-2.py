# -*- encoding: utf-8 -*-
# python 3.12
# g731. 110北二2.分數計算學習器
# 110北二區桃竹苗資訊學科能力複賽


from math import gcd

expr = input().split('+')
expr = [tuple(map(int, i.split('/'))) for i in expr]

while len(expr) > 1:
    expr[0] = expr[0][0] * expr[1][1] + expr[1][0] * expr[0][1], expr[0][1] * expr[1][1]
    expr.pop(1)
    g = gcd(*expr[0])
    expr[0] = expr[0][0] // g, expr[0][1] // g
    print('=' + '+'.join('/'.join(map(str, i)) for i in expr))
