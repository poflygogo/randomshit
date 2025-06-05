# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e941. pB. 分數式運算
# 2009大學學測推甄申請二階


from fractions import Fraction as Frac

expr = input().split()
expr[0] = Frac(expr[0])
for i in range(1, len(expr), 2):
    if expr[i] == '+':
        expr[0] += Frac(expr[i + 1])
    elif expr[i] == '-':
        expr[0] -= Frac(expr[i + 1])
print(f'{expr[0].numerator}/{expr[0].denominator}')
