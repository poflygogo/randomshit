# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q881. 快樂學幾何2


while True:
    try:
        print(pow(int(input().split()[1]), 2) // 2)
    except EOFError:
        break
