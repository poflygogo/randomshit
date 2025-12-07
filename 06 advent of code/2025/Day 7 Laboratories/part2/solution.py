# advent of code 2025
# Day 7 Laboratories
# Part 2
# python 3.12

import pathlib
from typing import TextIO

from functools import cache


class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[str] = input_file.read().splitlines()
        self.splitters: set[tuple[int, int]] = set()
        self.max_row: int = len(self.graph)
        self.max_col: int = len(self.graph[0])
        self.start: tuple[int, int] = (-1, -1)

        for r, row in enumerate(self.graph):
            for c, val in enumerate(row):
                if val == "S":
                    self.start = (r, c)
                elif val == "^":
                    self.splitters.add((r, c))

    def solve(self) -> int:
        @cache
        def dfs(row: int, col: int) -> int:
            if row >= self.max_row:
                return 1
            if (row, col) in self.splitters:
                return dfs(row + 1, col + 1) + dfs(row + 1, col - 1)
            return dfs(row + 1, col)

        return dfs(self.start[0], self.start[1])


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_path.exists():
        with input_path.open("r") as input_file:
            s = Solution(input_file)
            print(s.solve())
