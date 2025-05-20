# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q368. 3. 阿克曼函數
# 113學年度新北新莊高中校內資訊學科能力競賽


def ackermann(m, n):
    print((m, n))
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

print(ackermann(*map(int, input().split())))
