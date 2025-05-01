# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p904. 捷運 (MRT)
# TOI 練習賽 新手組

# 我討厭銀行家捨入法
from fractions import Fraction as Frac

count = int(input())
cost = sum(map(int, input().split()))

if count > 40:
    cost *= Frac(85, 100)
elif count > 20:
    cost *= Frac(90, 100)
elif count > 10:
    cost *= Frac(95, 100)

if cost > 1200:
    cost = 1200
elif cost.numerator % cost.denominator * 2 >= cost.denominator:
    cost += 1

print(cost.numerator // cost.denominator)
