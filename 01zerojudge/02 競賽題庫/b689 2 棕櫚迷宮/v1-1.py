# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b689. 2. 棕櫚迷宮


from typing import Tuple, Set


def find_entrance() -> Tuple[int, int]:
    for i in (0, max_row - 1):
        for j in range(max_row):
            if maze[i][j] == '.':
                return i, j
    for j in (0, max_col - 1):
        for i in range(1, max_row - 1):
            if maze[i][j] == '.':
                return i, j


def treasure(seen: Set[Tuple[int, int]], row: int, col: int):
    for i, j in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
        if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col and maze[i][j] == '.':
            seen.add((i, j))
            return treasure(seen, i, j)
    return row + 1, col + 1


max_row, max_col = map(int, input().split())
maze = [input() for _ in range(max_row)]
start_row, start_col = find_entrance()
print(*treasure({(start_row, start_col)}, start_row, start_col))
