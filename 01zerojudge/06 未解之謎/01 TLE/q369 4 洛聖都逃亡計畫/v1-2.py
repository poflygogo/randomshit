# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q369. 4. 洛聖都逃亡計畫


from collections import deque
from sys import stdin


def path_finder(graph: list, max_row: int, max_col: int) -> bool:
    start = find_start(graph, max_row, max_col)
    queue = deque([start])
    seen = set(queue)
    while queue:
        r, c = queue.popleft()
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if (i, j) not in seen and 0 <= i < max_row and 0 <= j < max_col:
                if graph[i][j] == 'T':
                    return True
                elif graph[i][j] == '.':
                    queue.append((i, j))
                seen.add((i, j))
    return False


def find_start(graph, max_row, max_col):
    for r in range(max_row):
        for c in range(max_col):
            if graph[r][c] == 'S':
                return r, c


def main():
    size, *graph = stdin.read().splitlines()
    if path_finder(graph, *map(int, size.split())):
        print('mission passed respect+')
    else:
        print('wasted')


if __name__ == '__main__':
    main()
