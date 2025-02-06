# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c676. 大家來出題 { 1: 簡易加法 }


import random


seen = set()
cnt = 100
while cnt > 0:
    a = random.randrange(1, int(1e6))
    b = random.randrange(1, int(1e6))
    c = a + b
    if c in seen:
        continue
    seen.add(c)
    cnt -= 1
    print(a, b, c)
