# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c517. 2. 南南見島


x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 <= x0 <= x2:
    print(min(abs(y1 - y0), abs(y2 - y0)))
elif y1 <= y0 <= y2:
    print(min(abs(x1 - x0), abs(x2 - x0)))
elif x0 < x1:
    print((x1 - x0) + min(abs(y1 - y0), abs(y2 - y0)))
elif x0 > x2:
    print((x0 - x2) + min(abs(y1 - y0), abs(y2 - y0)))
