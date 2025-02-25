# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12640 Largest Sum Game
# ZeroJudge i917


from sys import stdin

for arr in stdin:
    arr = tuple(map(int, arr.rstrip().split()))

    result = curr = 0
    for i in arr:
        curr = max(i, curr + i)
        result = max(result, curr)
    print(result)    
