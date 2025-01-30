# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h660. 躲避球 (DodgeBall)
# 2022-03 TOI 練習賽 新手組


x, r, v = map(int, input().split())
for _ in range(int(input())):
    p, s = map(int, input().split())
    if not (x - r <= p <= x + r):
        continue
    if s <= v:
        x = p
    elif p >= x:
        x -= 15
    else:
        x += 15

print(x)
