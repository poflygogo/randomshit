# advent of code 2025
# Day 9: Movie Theater
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple
from itertools import combinations


class Point(NamedTuple):
    row: int
    col: int


class Solution:
    def __init__(self, input_file: TextIO):
        self.all_points: list[Point] = []

        for line in input_file:
            col, row = map(int, line.strip().split(","))
            self.all_points.append(Point(row, col))

    def solve(self) -> int:
        return max(
            (abs(i.row - j.row) + 1) * (abs(i.col - j.col) + 1)
            for i, j in combinations(self.all_points, 2)
        )


if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_file.exists():
        with input_file.open() as f:
            s = Solution(f)
            print(s.solve())
    else:
        print("file no found")
