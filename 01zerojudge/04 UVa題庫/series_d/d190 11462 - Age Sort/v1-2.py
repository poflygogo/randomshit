# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11462 Age Sort
# ZeroJudge d190
# 
# Counting Sort

from sys import stdin


for line in stdin:
    line = int(line.rstrip())
    if not line:
        exit()
    
    counter = {}
    data = next(stdin).rstrip().split()
    for i in data:
        counter[i] = counter.get(i, -1) + 1
    
    data = sorted(counter, key=int)
    print(' '.join(i + (' ' + i) * counter[i] for i in data))
