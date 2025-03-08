# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b554. 5.貪吃龍遊戲


def dfs(path: set, row: int = 0, col: int = 0, depth: int = 0):
    if not (0 <= row < n and 0 <= col < n) or (graph[row][col] == '0') or (row, col) in path:
        global result
        result = max(result, depth)
        return
    depth += 1
    path.add((row, col))
    for i, j in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        dfs(path, row + i, col + j, depth)
    path.remove((row, col))


n = int(input())
graph = [input() for _ in range(n)]
result = 0
dfs(set())
print(result)
