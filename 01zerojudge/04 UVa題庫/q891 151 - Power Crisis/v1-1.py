# -*- encoding: utf-8 -*-
# python 3.12
# UVa 151 - Power Crisis
# ZeroJudge q891


k = 0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(1, 250):
        for j in range(1, n):
            k = (k + i) % j
        if k == 11:
            print(i)
            break
