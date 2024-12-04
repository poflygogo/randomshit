# -*- encoding: utf-8 -*-
# python 3.6
# zerojudge a810. 1. 倍數關係
# 102學年度高雄市資訊學科能力競賽複賽


from math import gcd


def lcm(arg1, arg2):
    """取兩個正整數的最小公倍數(for python 3.6)"""
    return abs(arg1 * arg2) // gcd(arg1, arg2)


def count_divisible(a: int, b: int, x: int, y: int) -> int:
    """
    統計 a 與 b 之間，有多少整數可以被 x 或 y 整除\n
    args:
        a, b: int, a < b
        x, y: int
    return:
        int, 表示一共有多少整數可以被 x 或 y 整除
    """
    is_abs = a * b > 0  # 若為真，表示 a, b 不為 0 且 a, b 同號
    if x == y == 0:
        if is_abs:
            return 0
        else:
            return 1

    x, y = sorted(map(abs, (x, y)))    
    if a * b > 0:
        a, b = sorted(map(abs, (a, b)))
        if x == 0:
            return b // y - a // y + bool(a % y == 0)
        if y % x == 0:
            return b // x - a // x + bool(a % x == 0)
        return (b // x - a // x + (a % x == 0)) + (b // y - a // y + (a % y == 0)) - (b // lcm(x, y) - a // lcm(x, y) + (a % lcm(x, y) == 0))

    if (x == 0) or (y % x == 0):
        return abs(a) // x + b // x + 1
    return (abs(a) // x + b // x + 1) + (abs(a) // y + b // y + 1) - (abs(a) // lcm(x, y) + b // lcm(x, y) + 1)


print(count_divisible(*map(int, input().split())))
