# -*- encoding: utf-8 -*-
# python 3.12
# UVa 498 Polly the Polynomial


def mainloop():
    from sys import stdin
    for line in stdin:
        line = tuple(map(int, line.rstrip().split()))
        nums = tuple(map(int, next(stdin).rstrip().split()))
        print(*calc_polynomial(line, nums))


def calc_polynomial(expr: tuple[int], nums: tuple[int]) -> list[int]:
    length = len(expr)
    result = []
    for x in nums:
        result.append(sum(expr[i] * x ** (length - i - 1) for i in range(length)))
    return result


mainloop()
