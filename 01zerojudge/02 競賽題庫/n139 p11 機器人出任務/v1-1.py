# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n139. p11. 機器人出任務
# 110 新北市資訊學科能力複賽


from collections import deque

max_col, max_row = map(int, input().split())
vertexes = [map(int, input().split()) for _ in range(int(input()))]
graph = [tuple(map(int, input().split())) for _ in range(max_row)]

steps = 0
b_y, b_x = vertexes.pop(0)
queue = deque()
seen = set()

while vertexes:
    a_x, a_y = b_x, b_y
    b_y, b_x = vertexes.pop(0)
    queue.append((a_x, a_y, 0))
    seen.add((a_x, a_y))
    while queue:
        r, c, cnt = queue.popleft()
        cnt += 1
        for i, j in ((r - 1, c - 1), (r - 1, c), (r - 1, c + 1), (r, c - 1), (r, c + 1), (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)):
            if 0 <= i < max_row and 0 <= j < max_col and (i, j) not in seen and graph[i][j] == 0:
                if (i, j) == (b_x, b_y):
                    steps += cnt
                    queue.clear()
                    break
                else:
                    seen.add((i, j))
                    queue.append((i, j, cnt))
    seen.clear()
print(steps)
