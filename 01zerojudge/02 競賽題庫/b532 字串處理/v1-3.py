# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b532. 字串處理

from string import digits
import operator

operate = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.floordiv,
           '%': operator.mod}

for _ in range(int(input())):
    text = input()
    op = ''
    expr = []
    for i in text:
        if i in digits:
            expr.append(i)
        elif (not op) and (i in operate):
            op = i
            expr.append(i)
    print(operate[op](*map(int, ''.join(expr).split(op))))
