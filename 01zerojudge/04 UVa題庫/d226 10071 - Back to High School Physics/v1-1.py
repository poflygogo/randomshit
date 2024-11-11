# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10071 Back to High School Physics
# ZeroJudge d226

while True:
    try:
        v, t = map(int, input().split())
    except EOFError:
        exit()
    else:
        print(2 * v * t)
