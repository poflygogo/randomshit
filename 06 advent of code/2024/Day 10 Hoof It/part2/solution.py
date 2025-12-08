# advent of code 2024
# day 10: hoof it
# part 1
# python 3.12

import pathlib
from typing import TextIO
from dataclasses import dataclass
from enum import Enum
from functools import cache


@dataclass(frozen=True)
class Point:
    row: int
    col: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.row + other.row, self.col + other.col)

    def __eq__(self, other: "Point"):
        if not isinstance(other, Point):
            return NotImplemented
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))


class Direction(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
    RIGHT = Point(0, 1)


class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[list[int]] = [
            [int(i) for i in line] for line in input_file.read().splitlines()
        ]
        self.max_row = len(self.graph)
        self.max_col = len(self.graph[0])

    def solve(self) -> int:
        result: int = 0
        for r, row in enumerate(self.graph):
            for c, val in enumerate(row):
                if val == 0:
                    result += self.calculate_score(r, c)
        return result

    def calculate_score(self, row: int, col: int) -> int:
        @cache
        def dfs(p: Point) -> int:
            if self.graph[p.row][p.col] == 9:
                return 1
            high: int = self.graph[p.row][p.col]
            total_path: int = 0
            for dir_p in Direction:
                next_p = p + dir_p.value
                if not self._is_valid_point(next_p):
                    continue
                next_high: int = self.graph[next_p.row][next_p.col]
                if next_high - high != 1:
                    continue
                total_path += dfs(next_p)
            return total_path

        return dfs(Point(row, col))

    def _is_valid_point(self, p: Point) -> bool:
        return 0 <= p.row < self.max_row and 0 <= p.col < self.max_col


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        solution = Solution(input_file)
        print(solution.solve())
