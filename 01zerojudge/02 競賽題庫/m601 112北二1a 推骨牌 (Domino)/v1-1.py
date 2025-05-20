# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m601. 112北二1a.推骨牌 (Domino)
# 112北二區桃竹苗資訊學科能力複賽


domino = [tuple(map(int, input().split())) for _ in range(int(input()))]
for i in range(1, len(domino)):
    x1, y1 = domino[i - 1]
    x2, y2 = domino[i]
    y2 /= 2
    if y1 ** 2 < (x2 - x1) ** 2 + y2 ** 2:
        print(x2)
        break
else:
    print(-1)
