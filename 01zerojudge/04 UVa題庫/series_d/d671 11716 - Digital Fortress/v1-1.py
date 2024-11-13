# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11716 Digital Fortress
# ZeroJudge d671

from math import sqrt


for _ in range(int(input())):
    code = input()
    length_sqrt = sqrt(len(code))
    if not length_sqrt.is_integer():
        print('INVALID')

    else:
        length_sqrt = int(length_sqrt)
        result = [
            code[idx]
            for col in range(length_sqrt)
            for idx in range(col, len(code), length_sqrt)
        ]

        print(*result, sep='')
