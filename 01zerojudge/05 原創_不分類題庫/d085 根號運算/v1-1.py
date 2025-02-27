# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d085. 根號運算


from sys import stdin
from collections import defaultdict
from functools import reduce
from operator import mul


def sqrt(n):
    if n in (0, 1):
        return n
    if n == -1:
        return 'i'
    
    if n < 0:
        is_imaginary = True
        n = abs(n)
    else:
        is_imaginary = False
    
    factors = defaultdict(int)
    while n % 2 == 0:
        n //= 2
        factors[2] += 1
    while n % 3 == 0:
        n //= 3
        factors[3] += 1
    for i in range(5, int(n ** 0.5) + 1, 6):
        for j in (i, i + 2):
            while n % j == 0:
                n //= j
                factors[j] += 1
    if n > 1:
        factors[n] = 1
    coefficient = 1
    for i in factors:
        if factors[i] > 1:
            k, factors[i] = divmod(factors[i], 2)
            coefficient *= i ** k
    radicand = reduce(mul, [i for i in factors if factors[i] != 0], 1)
    return (('' if (coefficient == 1 and radicand != 1) else f'{coefficient}') +
            (f'_/{radicand}' if radicand != 1 else '') +
            ('i' * is_imaginary))


for num in stdin:
    print(sqrt(int(num.rstrip())))
