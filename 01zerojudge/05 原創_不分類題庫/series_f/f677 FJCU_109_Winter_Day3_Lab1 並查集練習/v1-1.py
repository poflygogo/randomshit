# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f677. FJCU_109_Winter_Day3_Lab1 並查集練習

# ---------------------------------------------------

import sys
import io
Q = """
5 3
1 0
0 3
2 4
"""
sys.stdin = io.StringIO(Q.strip())

# --------------------------------------------------


n, m = map(int, input().split())

arr = list(range(n))

def find(x: int):
    if arr[x] == x:
        return x
    arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        x_root, y_root = sorted([x_root, y_root])
        arr[find(y)] = find(x)


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

root = find(0)
print(sum(find(i) == root for i in range(n)))
