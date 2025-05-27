# -*- encoding: utf-8 -*-
# python 3.12
# g731. 110北二2.分數計算學習器
# 110北二區桃竹苗資訊學科能力複賽


from fractions import Fraction as frac

expr = input().split('+')
expr[0] = frac(expr[0])

while len(expr) > 1:
    expr[0] += frac(expr.pop(1))
    print(f'={expr[0].numerator}/{expr[0].denominator}', *expr[1:], sep='+')
