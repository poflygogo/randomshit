# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i177. 小畫家 (Painter)
# 2022-04 TOI 練習賽 潛力組 第一題


import sys

sys.setrecursionlimit(30000)    # 沒事，我在發瘋


def dfs(r, c):
    if not (0 <= r < max_row) or not (0 <= c < max_col) or graph[r][c] != origin:
        return
    graph[r][c] = z
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


max_row, max_col, x, y, z = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(max_row)]

x -= 1
y -= 1
origin = graph[x][y]
if origin != z:
    dfs(x, y)

print('\n'.join(' '.join(map(str, row)) for row in graph))
