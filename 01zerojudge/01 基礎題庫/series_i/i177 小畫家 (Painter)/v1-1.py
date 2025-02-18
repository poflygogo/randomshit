# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i177. 小畫家 (Painter)
# 2022-04 TOI 練習賽 潛力組 第一題


max_row, max_col, x, y, z = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(max_row)]

x -= 1
y -= 1
origin = graph[x][y]

# bfs
queue = []
if origin != z:
    queue.append((x, y))
seen = set(queue)
while queue:
    r, c = queue.pop(0)
    graph[r][c] = z
    for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == origin:
            seen.add((i, j))
            queue.append((i, j))

print('\n'.join(' '.join(map(str, row)) for row in graph))
