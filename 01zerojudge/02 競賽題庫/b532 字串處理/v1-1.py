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
    expr = ''.join(filter(lambda x: x in digits or x in operator, text))
    for op in operator:
        if op in expr:
            print(operator[op](*map(int, expr.split(op))))
            break
