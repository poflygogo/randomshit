# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a881. C.什麼？油漆有毒？
# 102-1 延平資研社第二次練習賽


for _ in range(int(input())):
    _, w = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(w):
        k, *r = map(int, input().split())
        if k == 1:
            print(max(arr[r[0]:r[1] + 1]))
        elif k == 2:
            print(int(sum(arr[r[0]:r[1] + 1]) / abs(r[1] - r[0] + 1)))
        elif k == 3:
            print(arr[r[0]])
