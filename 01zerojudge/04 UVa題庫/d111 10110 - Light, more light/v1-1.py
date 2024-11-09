# -*- encoding: utf-8 -*-
# UVa 10110 Light, more light
# 求自然數 n 的因數有幾個，若為奇數則輸出 "yes"，若為偶數則輸出 "no"
# 此處的因數包含 1 和自然數 n 本身

from math import sqrt


while True:
    n = int(input())
    if not n:
        exit()
    elif sqrt(n).is_integer():
        print('yes')
    else:
        print('no')
