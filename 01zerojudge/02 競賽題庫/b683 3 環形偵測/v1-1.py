# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b683. 3. 環形偵測


# ---------------------------------------------------

# import sys
# import io
# Q = """
# 11 7
# .......
# .#####.
# .#...#.
# .#.#.#.
# .#...#.
# .#####.
# .......
# #######
# #....#.
# ..##.#.
# .###...
# """
# sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


from functools import reduce
from operator import mul


def dfs(path: set, r: int, c: int):
    if (r, c) == (row, col) and len(path) >= 4:
        seen.update(path)
        circle.append(len(path))
        return
    for i, j in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)):
        if 0 <= i < max_row and 0 <= j < max_col and graph[i][j] == '.' and (i, j) not in path:
            path.add((i, j))
            dfs(path, i, j)
            return


max_row, max_col = map(int, input().split())
graph = [input() for _ in range(max_row)]
circle = []
seen = set()
for row in range(max_row):
    for col in range(max_col):
        if graph[row][col] == '.' and (row, col) not in seen:
            dfs(set(), row, col)
print(len(circle), sum(circle), reduce(mul, circle, 1))
