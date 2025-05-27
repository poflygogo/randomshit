# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g730. 110北二1.矩形與點
# 110北二區桃竹苗資訊學科能力複賽


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
xp, yp = map(int, input().split())

x1, x2 = sorted([x1, x2])
y1, y2 = sorted([y1, y2])
x3, x4 = sorted([x3, x4])
y3, y4 = sorted([y3, y4])

if x3 < xp < x4 and y3 < yp < y4:
    print(0)

elif x1 < xp < x2 and y1 < yp < y2:
    print(1)

else:
    print(2)
