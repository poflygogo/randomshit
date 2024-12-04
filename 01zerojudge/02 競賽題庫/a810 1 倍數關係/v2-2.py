# -*- encoding: utf-8 -*-
# python 3.6
# zerojudge a810. 1. 倍數關係
# 102學年度高雄市資訊學科能力競賽複賽


# TODO: 當 x 或 y 至少有一個值為 0 且滿足某種未知條件時，將會輸出錯誤結果，找出該狀態並修正
from math import gcd


def lcm(arg1, arg2):
    """取兩個正整數的最小公倍數(for python 3.6)"""
    return abs(arg1 * arg2) // gcd(arg1, arg2)


a, b, x, y = map(int, input().split())

# testing code: 驗證答案是否正確
print(f'ans: {len([True for i in range(a, b + 1) if 0 in (x, y) or i % x == 0 or i % y == 0])}')

# 若 x, y 為負，將其轉換成正數，若為 0，則設為 1，並保證 x <= y
x, y = sorted(map(lambda n: abs(n) if n != 0 else 1, (x, y)))

# is_abs: a 和 b 同號或 a 與 b 其中一個為 0
# is_mul: x 是 y 的因數(gcd(x, y) == x)
is_abs, is_mul = a * b >= 0, y % x == 0

if is_abs and is_mul:
    a, b = sorted(map(abs, (a, b)))
    print(abs(b // x - a // x) + (a % x == 0))
elif is_abs and not is_mul:
    print((b // x - a // x + (a % x == 0)) + (b // y - a // y + (a % y == 0)) - (b // lcm(x, y) - a // lcm(x, y) + (a % lcm(x, y) == 0)))
elif not is_abs and is_mul:
    print(abs(a) // x + b // x + 1)
else:   # if not is_abs and not is_mul
    print((abs(a) // x + b // x + 1) + (abs(a) // y + b // y + 1) - (abs(a) // lcm(x, y) + b // lcm(x, y) + 1))
