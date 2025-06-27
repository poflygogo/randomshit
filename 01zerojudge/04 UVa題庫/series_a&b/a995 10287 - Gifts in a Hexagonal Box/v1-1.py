# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10287 Gifts in a Hexagonal Box
# ZeroJudge a995

sqrt3 = 3**0.5
sqrt7 = 7**0.5
while True:
    try:
        n = float(input())
        print(
            f"{n / 2 * sqrt3:.10f}",
            f"{n * 3 / (3 + 2 * sqrt3):.10f}",
            f"{n / 2 * sqrt3 / 2:.10f}",
            f"{n * (6 * sqrt7 - 7 * sqrt3) / 10:.10f}",
        )
    except EOFError:
        break
