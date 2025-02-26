# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12970 Alcoholic Pilots
# ZeroJudge h385


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

v1, d1, v2, d2 = map(int, input().split())
test_case = 1
beer = ('No beer for the captain.', 'You owe me a beer!')
while any((v1, d1, v2, d2)):
    d1, d2 = d1 * v2, d2 * v1
    v1 = v2 = v1 * v2
    winner = beer[bool(d1 < d2)]
    
    v1 *= 2
    d1 += d2
    g = gcd(v1, d1)
    d1 //= g
    v1 //= g
    if v1 == 1:
        avg = str(d1)
    else:
        avg = f'{d1}/{v1}'

    print(f'Case #{test_case}: {winner}\nAvg. arrival time: {avg}')
    test_case += 1
    v1, d1, v2, d2 = map(int, input().split())
