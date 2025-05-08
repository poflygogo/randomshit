# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a831. 1、地砖摆放
# 备战 NOIP 2013模拟赛系列


from math import ceil

n, m, a = map(int, input().split())
print(ceil(n / a) * ceil(m / a))
