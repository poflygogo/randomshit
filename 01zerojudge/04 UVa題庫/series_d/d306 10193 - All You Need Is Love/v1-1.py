# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10193 - All You Need Is Love
# ZeroJudge d306

from math import gcd


for case in range(1, int(input()) + 1):
    s1, s2 = int(input().rstrip(), base=2), int(input().rstrip(), base=2)
    print(
        f'Pair #{case}:',
        'All you need is love!' if gcd(s1, s2) not in (0, 1) else
        'Love is not all you need!'
    )
