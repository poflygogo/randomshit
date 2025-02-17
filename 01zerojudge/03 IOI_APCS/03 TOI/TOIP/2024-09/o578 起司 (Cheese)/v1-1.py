# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o578. 起司 (Cheese)
# 2024-09 TOI 練習賽 新手組 第一題


a, b, c, d = map(int, input().split())
if any(i % d != 0 for i in (a, b, c)):
    print(0)
else:
    print((a // d) * (b // d) * (c // d))
