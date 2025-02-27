# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10336 Rank the Languages
# ZeroJudge d365


for t in range(1, int(input()) + 1):
    max_row, max_col = map(int, input().split())
    graph = [input() for _ in range(max_row)]

    result = {}
    seen = set()
    for row in range(max_row):
        for col in range(max_col):
            if (row, col) in seen:
                continue
            result[graph[row][col]] = result.get(graph[row][col], 0) + 1
            queue = [(row, col)]
            seen.add((row, col))
            while queue:
                r, c = queue.pop(0)
                for i, j in ((r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)):
                    if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == graph[row][col]:
                        seen.add((i, j))
                        queue.append((i, j))
    print(f'World #{t}',
          '\n'.join(f'{i}: {result[i]}' for i in sorted(result, key=lambda x: (-result[x], x))),
          sep='\n')
