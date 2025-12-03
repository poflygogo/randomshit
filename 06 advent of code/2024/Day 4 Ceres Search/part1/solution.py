# advent of code 2024
# Day 4: Ceres Search
# Part 1
# python 3.12

import pathlib
from typing import TextIO

DIRECTIONS: tuple[tuple[int, int]] = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
)


def solve(input_file: TextIO) -> int:
    graph: list[str] = input_file.read().splitlines()

    max_row: int = len(graph)
    max_col: int = len(graph[0])
    cnt: int = 0

    for row in range(max_row):
        for col in range(max_col):
            if graph[row][col] != "X":
                continue
            for d_row, d_col in DIRECTIONS:
                e_row = row + d_row * 3  # 4 = len("XMAS") - 1
                e_col = col + d_col * 3
                if not (0 <= e_row < max_row and 0 <= e_col < max_col):
                    continue
                text: list[str] = [
                    graph[row + i * d_row][col + i * d_col] for i in range(4)
                ]
                if all(i == j for i, j in zip("XMAS", text)):
                    cnt += 1
    return cnt


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        print(solve(input_file))
