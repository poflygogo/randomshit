# -*- encoding: utf-8 -*-
# python 3.12
# UVa 01585 Score
# ZeroJudge e540


from itertools import groupby


for _ in range(int(input())):
    data = groupby(input())

    result = 0
    for _, i in data:
        i = tuple(i)
        if i[0] == 'O':
            n = len(i)
            result += (1 + n) * n // 2
    
    print(result)
