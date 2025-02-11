# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d626. 小畫家真好用


def bfs(row: int, col: int):
    queue = [(row, col)]
    visited = {(row, col)}
    while queue:
        r, c = queue.pop(0)
        graph[r][c] = '+'
        for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if (i, j) in visited:
                continue
            if 0 <= i < n and 0 <= j < n and graph[i][j] == '-':
                queue.append((i, j))
                visited.add((i, j))


n = int(input())
graph = [list(input()) for _ in range(n)]
bfs(*map(int, input().split()))
print('\n'.join(''.join(r) for r in graph))
