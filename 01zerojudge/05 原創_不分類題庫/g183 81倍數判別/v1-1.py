# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g183. 81倍數判別


while True:
    try:
        print(
            'konopad!' if int(input()) % 81 == 0 else
            'konosuba!'
        )
    except EOFError:
        break
