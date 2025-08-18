# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11202 - The Least Possible Effort
# ZeroJudge q909

# 不用真的遍歷所有結果，圖形是有對稱關係的，所以只需要遍歷四分之一的棋盤就好

from math import ceil

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(ceil(a / 2) * ceil(b / 2))
