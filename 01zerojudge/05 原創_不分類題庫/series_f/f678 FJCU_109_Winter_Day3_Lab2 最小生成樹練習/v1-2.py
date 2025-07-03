# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f678. FJCU_109_Winter_Day3_Lab2 最小生成樹練習


# ---------------------------------------------------

import sys
import io

Q = """
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


n, m = map(int, input().split())

items = list(range(n))


def find(x: int):
    if items[x] == x:
        return x
    items[x] = find(items[x])
    return items[x]


def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        items[y_root] = x_root
        return True
    else:
        return False


graph = [tuple(map(int, input().split())) for _ in range(m)]
graph.sort(key=lambda x: x[2])

result = 0
edge_cnt = 0
for u, v, w in graph:
    if edge_cnt == n - 1:
        break
    if union(u, v):
        result += w
        edge_cnt += 1

print(result)
