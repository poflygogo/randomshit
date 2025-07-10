# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c463. apcs 樹狀圖分析 (Tree Analyses)

# ---------------------------------------------------

import sys
import io
Q = """
9 
1 6 
3 5 3 8 
0 
2 1 7 
1 9 
0 
1 2 
0 
0 
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



n = int(input())

arr = list(range(n + 1))
leaf = set()

# 紀錄樹的結構，並將葉節點標記起來
for i in range(1, n + 1):
    cnt, *children = map(int, input().split())
    if cnt:
        for j in children:
            arr[j] = i
    else:
        leaf.add(i)

# 紀錄各節點的高度
height = [0] * (n + 1)
for node in leaf:
    node = arr[node]
    cnt = 0
    while True:
        cnt += 1
        if height[node] >= cnt:
            break
        height[node] = cnt
        if arr[node] == node:
            break
        node = arr[node]

print(height.index(max(height)))
print(sum(height))
