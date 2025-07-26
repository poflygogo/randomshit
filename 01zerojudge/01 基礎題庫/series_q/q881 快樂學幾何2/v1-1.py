# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q881. 快樂學幾何2


while True:
    try:
        _, b = map(int, input().split())
        print(b * b // 2)
    except EOFError:
        break
