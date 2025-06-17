# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q836. 1. 小心陷阱
# 2025年6月APCS


k = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

locate = 0
while k > 0:
    locate += k
    if locate % x1 == 0:
        k -= y1
    if locate % x2 == 0:
        k -= y2

print(locate)
