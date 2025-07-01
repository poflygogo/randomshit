# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f671. FJCU_109_Winter_Day1_Lab6 最短路徑

# ---------------------------------------------------

import sys
import io
Q = """
3 5
.#...
.#.#.
...#.
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


class Node:
    def __init__(self, row, col, step):
        self.row = row
        self.col = col
        self.step = step


def bfs():
    queue = [Node(0, 0, 0)]
    seen = {(0, 0)}
    while queue:
        v = queue.pop(0)
        step = v.step + 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            tr, tc = v.row + dr, v.col + dc
            if (tr, tc) == target:
                return step
            if (tr, tc) not in seen and 0 <= tr < max_row and 0 <= tc < max_col and graph[tr][tc] == '.':
                queue.append(Node(tr, tc, step))
                seen.add((tr, tc))
    return -1


max_row, max_col = map(int, input().split())
graph = [input() for _ in range(max_row)]

target = (max_row - 1, max_col - 1)
print(bfs())
