# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c676. 大家來出題 { 1: 簡易加法 }


import random


for _ in range(100):
    a = random.randrange(-int(1e6) + 1, int(1e6))
    b = random.randrange(-int(1e6) + 1, int(1e6))
    c = a + b
    print(a, b, c)
