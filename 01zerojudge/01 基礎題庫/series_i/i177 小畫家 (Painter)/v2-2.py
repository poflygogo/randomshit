# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i177. 小畫家 (Painter)
# 2022-04 TOI 練習賽 新手組 第一題


max_row, max_col, x, y, z = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(max_row)]

x -= 1
y -= 1
origin = graph[x][y]

# dfs
stack = []
if origin != z:
    stack.append((x, y))
seen = set(stack)
while stack:
    r, c = stack.pop()
    graph[r][c] = z
    for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == origin:
            stack.append((i, j))
            seen.add((i, j))
    

print('\n'.join(' '.join(map(str, row)) for row in graph))
