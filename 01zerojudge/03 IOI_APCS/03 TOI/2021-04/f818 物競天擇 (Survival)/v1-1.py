# -*- encoding: utf-8 -*-
# python 3.12
# TOI 練習賽 2021-04 新手組 第一題
# ZeroJudge f818


input()
print(*min(zip(input().split(), input().split()), key=lambda x: int(x[0]) * int(x[1])))
