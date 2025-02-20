# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00722 Lakes
# ZeroJudge e550


from collections import deque

t = int(input())
input()
queue = deque()
seen = set()
graph = []
for _ in range(t):
    row, col = map(int, input().split())
    row -= 1
    col -= 1
    while True:
        try:
            line = input()
            if line:
                graph.append(line)
            else:
                break
        except EOFError:
            break
    
    max_row, max_col = len(graph), len(graph[0])
    queue.append((row, col))
    seen.add((row, col))
    while queue:
        r, c = queue.popleft()
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= i < max_row and 0 <= j < max_col and (i, j) not in seen and graph[i][j] == '0':
                seen.add((i, j))
                queue.append((i, j))

    print(len(seen))
    queue.clear()
    seen.clear()
    graph.clear()
