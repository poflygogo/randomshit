# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o168. 電子畫布 s


h, w, n = [int(i) for i in input().split()]
tt = [[0 for i in range(w)] for j in range(h)]


for j in range(n):
    r, c, t, x = [int(i) for i in input().split()]
    for y in range(r - t, r + t + 1):
        if y < 0 or y > h - 1:
            continue
        ydif = abs(r - y)
        for x in range(c - (t - ydif), c + (t - ydif) + 1):
            if x < 0 or x > w - 1:
                continue
            tt[y][x] += x

for i in tt:
    for j in i:
        print(j, end=" ")
    print()
