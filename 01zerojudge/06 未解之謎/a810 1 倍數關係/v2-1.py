# -*- encoding: utf-8 -*-
# python 3.6
# zerojudge a810. 1. 倍數關係
# 102學年度高雄市資訊學科能力競賽複賽


from math import gcd


def lcm(arg1, arg2):
    return abs(arg1 * arg2 // gcd(arg1, arg2))


a, b, x, y = map(int, input().split())
x, y = sorted(map(lambda n: abs(n) if n != 0 else 1, (x, y)))
is_abs, is_mul = a * b >= 0, y % x == 0

if is_abs and is_mul:
    print(abs(b) // x - abs(a) // x + (a % x == 0))
elif is_abs and not is_mul:
    print((b // x - a // x + (a % x == 0)) + (b // y - a // y + (a % y == 0)) - (b // lcm(x, y) - a // lcm(x, y) + (a % lcm(x, y) == 0)))
elif not is_abs and is_mul:
    print(abs(a) // x + b // x + 1)
else:
    print((abs(a) // x + b // x + 1) + (abs(a) // y + b // y + 1) - (abs(a) // lcm(x, y) + b // lcm(x, y) + 1))