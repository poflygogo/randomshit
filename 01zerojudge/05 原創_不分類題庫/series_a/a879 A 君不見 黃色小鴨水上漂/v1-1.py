# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a879. A.君不見 黃色小鴨水上漂
# 102-1 延平資研社第二次練習賽


for _ in range(int(input())):
    n, s = map(int, input().split())
    s **= 2
    duck = [tuple(map(int, input().split())) for _ in range(n)]
    x0, y0 = map(int, input().split())
    count = 0
    for x, y in duck:
        if (x - x0) ** 2 + (y - y0) ** 2 <= s:
            count += 1
    print(count)
