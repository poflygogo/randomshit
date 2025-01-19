# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f341. 5.閱讀順序(Reading)
# 2020-08 TOI 新手同好會


a, b, c = input().partition(input())
print(c[::-1] + b + a[::-1])
