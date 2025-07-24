# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e180. Runningman - 撕名牌大戰


while True:
    n = int(input())
    if n == 0:
        break
    arr = map(int, input().split())
    result = 0
    curr = next(arr)
    for i in arr:
        if i > curr:
            result += i - curr
        curr = i
    print(result)
