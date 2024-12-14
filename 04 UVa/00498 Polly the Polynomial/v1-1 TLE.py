# -*- encoding: utf-8 -*-
# python 3.12
# UVa 498 Polly the Polynomial


def mainloop():
    while True:
        try:
            print(*calc_polynomial(
                tuple(map(int, input().split())),
                tuple(map(int, input().split()))
            ))
        except EOFError:
            break


def calc_polynomial(expr: tuple[int], nums: tuple[int]) -> list[int]:
    length = len(expr) - 1
    result = []
    for x in nums:
        result.append(sum(j * x ** (length - i) for i, j in enumerate(expr)))
    return result


mainloop()
