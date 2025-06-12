# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e665. 108 p3. 彩珠的計算
# 108新北市資訊學科能力複賽 


def color_beads(n: int, r: int=0, g: int=0, b: int=0, depth: int= 0):
    if n == depth:
        return r, g, b
    total_beads = 2 ** depth
    i, j = divmod(total_beads, 3)
    r += i + (j >= 1)
    g += i + (j >= 2)
    b += i
    return color_beads(n, r, g, b, depth + 1)


for i in range(1, 30):
    print(f'{i} -> {" ".join(map(str, color_beads(i)))}')
