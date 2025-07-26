# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q889. 快樂學幾何3


while True:
    try:
        a, b, c, d = map(int, input().split())
        print(c - b + a - d)
    except EOFError:
        break
