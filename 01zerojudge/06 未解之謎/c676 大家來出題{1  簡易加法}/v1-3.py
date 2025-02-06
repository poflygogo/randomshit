# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c676. 大家來出題 { 1: 簡易加法 }


import random


cnt = 0
seen = set()
while cnt < 100:
    a = random.randrange(-int(1e6) + 1, int(1e6))
    b = random.randrange(-int(1e6) + 1, int(1e6))
    c = a + b
    if 0 in (a, b) or c in seen:
        continue
    cnt += 1
    seen.add(c)
    print(a, b, c)
