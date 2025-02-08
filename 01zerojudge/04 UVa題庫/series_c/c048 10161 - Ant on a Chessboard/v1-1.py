# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10161 Ant on a Chessboard
# ZeroJudge c048


from sys import stdin
import math


for n in stdin:
    n = int(n.rstrip())
    if not n:
        break
    depth = math.sqrt(n)
    depth = math.floor(depth) + (not depth.is_integer())
    mid = (depth - 1) ** 2 + depth
    row, col = depth, depth - abs(mid - n)
    if n > mid:
        row, col = col, row
    if depth & 1:
        row, col = col, row
    print(col, row)
