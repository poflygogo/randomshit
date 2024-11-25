# -*- encodingL utf-8 -*-
# python 3.12
# zerojudge a788. 10. uPhone Two-Point Zoom
# HP CodeWars 2008


from math import sqrt, atan, ceil


while True:
    # x{第 n 根手指}{開始 or 結束}
    x11, y11, x12, y12, x21, y21, x22, y22 = map(float, input().split())
    if x11 == y11 == x12 == y12 == x21 == y21 == x22 == y22 == 0:
        break

    # rd: relative displacement 相對位移
    # 結束兩點的中點 - 開始兩點的中點
    rd_X = ((x12 + x22) - (x11 + x21)) / 2
    rd_y = ((y12 + y22) - (y11 + y21)) / 2

    # 當數值為負時，應向上取整
    if rd_X < 0:
        rd_X = ceil(rd_X)
    else:
        rd_X = int(rd_X)

    if rd_y < 0:
        rd_y = ceil(rd_y)
    else:
        rd_y = int(rd_y)

    # zoom: 縮放倍率(放大率)
    # 結束時兩點的距離 / 開始時兩點的距離
    zoom = sqrt((x22 - x12) ** 2 + (y22 - y12) ** 2) / sqrt((x21 - x11) ** 2 + (y21 - y11) ** 2)

    # ra: rotation angle 旋轉角度(逆時針)
    # ra = tan(結束時兩點的斜率) - tan(開始時兩點的斜率)
    ra = (atan((y22 - y12) / (x22 - x12))) - (atan((y21 - y11) / (x21 - x11)))
    ra = f'{ra:.3f}'
    if ra == '-0.000': ra = '0.000' 

    print(f'{rd_X} {rd_y} {zoom:.3f} {ra}')
