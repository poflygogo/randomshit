# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q369. 4. 洛聖都逃亡計畫


from collections import deque
from sys import stdin


def path_finder(graph: list, max_row: int, max_col: int) -> bool:
    def find_start_end():
        s = e = None
        for r in range(max_row):
            for c in range(max_col):
                if None in (s, e):
                    if s is None and graph[r][c] == 'S':
                        s = (r, c)
                    elif e is None and graph[r][c] == 'T':
                        e = (r, c)
                graph[r][c] = bool(graph[r][c] == '.')
        return s, e

    def neighbor(r: int, c: int):
        for i, j in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= i < max_row and 0 <= j < max_col and graph[i][j]:
                yield i, j

    def expand(queue: deque, seen_self: set, seen_other: set) -> bool:
        node = queue.popleft()
        for r, c in neighbor(*node):
            if (r, c) in seen_other:
                return True
            if (r, c) not in seen_self:
                seen_self.add((r, c))
                queue.append((r, c))
        return False

    start, end = find_start_end()
    queue_s, queue_e = deque([start]), deque([end])
    seen_s, seen_e = set(queue_s), set(queue_e)
    while queue_s and queue_e:
        if expand(queue_s, seen_s, seen_e) or expand(queue_e, seen_e, seen_s):
            return True
    return False


def main():
    size, *graph = stdin.read().splitlines()
    if path_finder(list(map(list, graph)), *map(int, size.split())):
        print('mission passed respect+')
    else:
        print('wasted')


if __name__ == '__main__':
    main()
