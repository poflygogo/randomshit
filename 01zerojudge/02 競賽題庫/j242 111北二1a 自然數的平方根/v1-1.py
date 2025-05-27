# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j242. 111北二1a.自然數的平方根
# 111北二區桃竹苗資訊學科能力複賽


from functools import reduce
from operator import mul

n = int(input())

factor = {}
for p in (2, 3):
    while n % p == 0:
        factor[p] = factor.get(p, 0) + 1
        n //= p

for p in range(5, int(n ** 0.5) + 1, 6):
    while n % p == 0:
        factor[p] = factor.get(p, 0) + 1
        n //= p
    if n < p:
        break
    p += 2
    while n % p == 0:
        factor[p] = factor.get(p, 0) + 1
        n //= p
    if n < p:
        break

if n != 1:
    factor[n] = 1

a = 1
for i in factor:
    if factor[i] >= 2:
        a *= i ** (factor[i] // 2)
        factor[i] %= 2


b = reduce(mul, [i ** j for i, j in factor.items()], 1)

print('' if a == 1 else a,
      '' if b == 1 else f'sqrt({b})',
      sep=' ')
