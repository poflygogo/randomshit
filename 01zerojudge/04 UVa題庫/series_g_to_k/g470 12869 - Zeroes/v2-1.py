# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12869 Zeroes
# ZeroJudge g470


a, b = map(int, input().split())
while not (a == b == 0):
    print(b // 5 - a // 5 + 1)
    a, b = map(int, input().split())
