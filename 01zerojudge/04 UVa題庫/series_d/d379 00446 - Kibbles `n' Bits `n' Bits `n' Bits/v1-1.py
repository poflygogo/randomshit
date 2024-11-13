# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00446 Kibbles `n' Bits `n' Bits `n' Bits
# ZeroJudge d379

for _ in range(int(input())):
    expr = input().split()
    num1, num2 = int(expr[0], base=16), int(expr[2], base=16)
    print(f'{num1:013b} {expr[1]} {num2:013b} = {num1 + num2 if expr[1] == "+" else num1 - num2}')
