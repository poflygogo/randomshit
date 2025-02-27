# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10336 Rank the Languages
# ZeroJudge d365


def dfs(r, c):
    if not (0 <= r < max_row) or not (0 <= c < max_col) or graph[r][c] is None or graph[r][c] != target:
        return
    graph[r][c] = None
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)


for t in range(1, int(input()) + 1):
    max_row, max_col = map(int, input().split())
    graph = [list(input()) for _ in range(max_row)]

    result = {}
    for row in range(max_row):
        for col in range(max_col):
            if graph[row][col] is None:
                continue
            result[graph[row][col]] = result.get(graph[row][col], 0) + 1
            target = graph[row][col]
            dfs(row, col)
    print(f'World #{t}',
          '\n'.join(f'{i}: {result[i]}' for i in sorted(result, key=lambda x: (-result[x], x))),
          sep='\n')
