# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o712. 2. 蒐集寶石
# 2024-10 APCS


max_row, max_col, k, row, col = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(max_row)]

score = 0
count = 0
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))
turn = 0

while graph[row][col] != 0:
    count += 1
    score += graph[row][col]
    graph[row][col] -= 1

    if score % k == 0:
        turn = (turn + 1) % 4

    while (not (0 <= row + direction[turn][0] < max_row) or 
           not (0 <= col + direction[turn][1] < max_col) or
           (graph[row + direction[turn][0]][col] == -1) or
           (graph[row][col + direction[turn][1]] == -1)):
        turn = (turn + 1) % 4
    
    row += direction[turn][0]
    col += direction[turn][1]

print(count)
