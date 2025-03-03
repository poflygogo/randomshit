# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b532. 字串處理

from string import digits

operator = {'+': int.__add__,
            '-': int.__sub__,
            '*': int.__mul__,
            '/': int.__floordiv__,
            '%': int.__mod__}

for _ in range(int(input())):
    text = input()
    op = ''
    expr = []
    for i in text:
        if i in digits:
            expr.append(i)
        elif (not op) and (i in operator):
            op = i
            expr.append(i)
    print(operator[op](*map(int, ''.join(expr).split(op))))
