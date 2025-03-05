# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00834 Continued Fractions
# ZeroJudge k932


from sys import stdin

for line in stdin:
    a, b = map(int, line.rstrip().split())
    numerate, a = divmod(a, b)
    result = []
    while a != 0:
        t, b = divmod(b, a)
        a, b = b, a
        result.append(t)
    print(f'[{numerate}{";" if result else ""}{",".join(map(str, result))}]')
