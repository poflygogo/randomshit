# advent of code 2024
# Day 4 Ceres Search
# Part 2
# python 3.12

import pathlib
from typing import TextIO


def solve(input_file: TextIO) -> int:
    graph: list[str] = input_file.read().splitlines()

    max_row: int = len(graph)
    max_col: int = len(graph[0])
    cnt: int = 0

    for row in range(1, max_row - 1):
        for col in range(1, max_col - 1):
            if graph[row][col] != "A":
                continue
            text1: str = "".join(
                graph[i][j]
                for i, j in zip(range(row - 1, row + 2), range(col - 1, col + 2))
            )
            text2: str = "".join(
                graph[i][j]
                for i, j in zip(range(row - 1, row + 2), range(col + 1, col - 2, -1))
            )
            if text1 not in ("MAS", "SAM"):
                continue
            if text2 not in ("MAS", "SAM"):
                continue
            cnt += 1

    return cnt


if __name__ == "__main__":
    input_path: TextIO = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open("r") as file:
        print(solve(file))
