# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10287 Gifts in a Hexagonal Box
# ZeroJudge a995


sqrt3 = 3**0.5
sqrt7 = 7**0.5
calc = [
    lambda n: n / 2 * sqrt3,
    lambda n: n * 3 / (3 + 2 * sqrt3),
    lambda n: n / 2 * sqrt3 / 2,
    lambda n: n * (6 * sqrt7 - 7 * sqrt3) / 10,
]
while True:
    try:
        n = float(input())
        print(*[f"{func(n):.10f}" for func in calc])
    except EOFError:
        break
