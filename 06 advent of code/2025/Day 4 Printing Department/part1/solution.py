# advent of code 2025
# day 4 printing department
# part 1
# python 3.12

import pathlib
from typing import TextIO


def solve(input_file: TextIO) -> int:
    graph: list[str] = input_file.read().splitlines()

    max_row: int = len(graph)
    max_col: int = len(graph[0])

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
    result: int = 0
    for row in range(max_row):
        for col in range(max_col):
            if graph[row][col] != "@":
                continue
            near_cnt: int = 0
            for dr, dc in DIRECTIONS:
                nr: int = row + dr
                nc: int = col + dc
                if nr < 0 or nr >= max_row or nc < 0 or nc >= max_col:
                    continue
                if graph[nr][nc] == "@":
                    near_cnt += 1
                if near_cnt >= 4:  # early exit
                    break
            if near_cnt < 4:
                result += 1

    return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        print(solve(input_file))
