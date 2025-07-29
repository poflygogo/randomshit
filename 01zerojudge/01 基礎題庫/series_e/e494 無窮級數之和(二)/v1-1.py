# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e494. 無窮級數之和(二)


from decimal import Decimal

m = Decimal("0.261_497_212_847_642")
p = Decimal(input())

print(round(p.ln().ln() + m, 3))
