# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a810. 1. 倍數關係
# 102學年度高雄市資訊學科能力競賽複賽

from math import lcm


a, b, x, y = map(int, input().split())
if a >= 0:
    b -= a
    print(b // x + b // y - b // lcm(x, y) + 1)
else:
    a = abs(a)
    print(
        a // x + a // y - a // lcm(x, y) +
        b // x + b // y - b // lcm(x, y) + 
        1
    )