"""
https://www.bilibili.com/video/BV1mp4y1D7UP?p=6&vd_source=be047ab4bf72139c16fdaee5dc683006
"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f'moving from {a} to {c}')
        hanoi(n -1, b, a, c)

hanoi(3, 'A', 'B', 'C')
