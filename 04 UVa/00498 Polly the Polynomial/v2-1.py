# -*- encoding: utf-8 -*-
# python 3.12
# UVa 498 Polly the Polynomial


def mainloop():
    from sys import stdin
    for line in stdin:
        line = list(map(int, line.rstrip().split()))
        line = line[::-1]
        nums = tuple(map(int, next(stdin).rstrip().split()))
        print(*calc_polynomial(line, nums))


def calc_polynomial(expr: list[int], nums: tuple[int]) -> list[int]:
    length = len(expr)
    result = []
    for x in nums:
        temp = 1
        total = 0
        for n in expr:
            total += n * temp
            temp *= x
        result.append(total)
    return result


mainloop()
