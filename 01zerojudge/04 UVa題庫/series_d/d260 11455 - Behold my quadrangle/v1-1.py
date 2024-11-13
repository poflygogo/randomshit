# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11455 Behold my quadrangle
# ZeroJudge d260

for _ in range(int(input())):
    a, b, c, d = sorted(map(int, input().split()))
    if a == b == c == d:
        print('square')
    elif a == b and c == d and a != c:
        print('rectangle')
    elif a + b + c > d:
        print('quadrangle')
    else:
        print('banana')
