# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i177. 小畫家 (Painter)
# 2022-04 TOI 練習賽 潛力組 第一題


from collections import deque
from array import array
from sys import stdin

scan = stdin.readline
max_row, max_col, x, y, z = map(int, scan().rstrip().split())
graph = [array('H', (map(int, scan().rstrip().split()))) for _ in range(max_row)]

x -= 1
y -= 1
origin = graph[x][y]

# bfs
queue = deque()
if origin != z:
    queue.append((x, y))
seen = set(queue)
while queue:
    r, c = queue.popleft()
    graph[r][c] = z
    for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
        if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == origin:
            seen.add((i, j))
            queue.append((i, j))

print('\n'.join(' '.join(map(str, row)) for row in graph))
