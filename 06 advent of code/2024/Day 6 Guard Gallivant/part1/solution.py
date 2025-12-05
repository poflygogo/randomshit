# advent of code 2024
# day 6 guard gallivant
# part 1
# python 3.12

import pathlib
from typing import TextIO

from enum import Enum


class Direction(Enum):
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

    def next(self) -> "Direction":
        lst: list[Direction] = list(Direction)
        idx: int = lst.index(self)
        next_idx: int = (idx + 1) % len(lst)
        return lst[next_idx]


def solve(input_file: TextIO) -> int:
    graph: list[str] = input_file.read().splitlines()
    max_rows: int = len(graph)
    max_cols: int = len(graph[0])

    def find_start() -> tuple[int, int]:
        for i, line in enumerate(graph):
            if "^" in line:
                return i, line.index("^")

    r, c = find_start()
    dir: Direction = Direction.UP
    visited: set[tuple[int, int]] = {(r, c)}
    while True:
        visited.add((r, c))
        nr, nc = r + dir.value[0], c + dir.value[1]
        if nr < 0 or nr >= max_rows or nc < 0 or nc >= max_cols:
            break
        elif graph[nr][nc] == "#":
            dir = dir.next()
        else:
            r, c = nr, nc

    return len(visited)


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        print(solve(input_file))
