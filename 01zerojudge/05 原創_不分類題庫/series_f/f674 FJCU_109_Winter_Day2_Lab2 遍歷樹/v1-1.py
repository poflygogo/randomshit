# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f674. FJCU_109_Winter_Day2_Lab2 遍歷樹

# ---------------------------------------------------

import sys
import io
Q = """
8
0 1 3
1 6 2
2 4 -1
3 7 5
4 -1 -1
5 -1 -1
6 -1 -1
7 -1 -1
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------
#      0
#    /   \
#   1     3
#  / \   / \
# 6   2 7   5
#    /
#   4


tree = {}
for _ in range(int(input())):
    parent, *child = map(int, input().split())
    tree[parent] = child


def prefix(arr: list, node: int = 0):
    if node != -1:
        arr.append(node)
        prefix(arr, tree[node][0])
        prefix(arr, tree[node][1])


def infix(arr: list, node: int = 0):
    if node != -1:
        infix(arr, tree[node][0])
        arr.append(node)
        infix(arr, tree[node][1])


def postfix(arr: list, node: int = 0):
    if node != -1:
        postfix(arr, tree[node][0])
        postfix(arr, tree[node][1])
        arr.append(node)


a, b, c = [], [], []
prefix(a)
infix(b)
postfix(c)

print(*a)
print(*b)
print(*c)
