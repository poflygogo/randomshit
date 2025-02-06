# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c635. 基礎排序 #1-2 ( 位置排序 )


from sys import stdin
from itertools import zip_longest


for line in stdin:
    line = line.strip().split(',')
    arr_even = line[::2]
    arr_odd = line[1::2]
    arr_even.sort(key=int)
    arr_odd.sort(key=int)
    print(','.join(i for pair in zip_longest(arr_even, arr_odd, fillvalue=None) for i in pair if i is not None))
