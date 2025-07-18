# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p906. 食譜換算 (Recipe)
# TOI練習賽202504新手組第1題


from math import ceil
from fractions import Fraction as Frac
n, a = map(int, input().split())
arr = list(map(int, input().split()))
b = arr.pop()
mul = Frac(b, a)
print(' '.join(str(ceil(i * mul)) for i in arr))
