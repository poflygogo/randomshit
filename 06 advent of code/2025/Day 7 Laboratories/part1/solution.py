# advent of code 2025
# Day 7 Laboratories
# Part 1
# python 3.12

import pathlib
from typing import TextIO


class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[str] = input_file.read().splitlines()
        self.max_row: int = len(self.graph)
        self.max_col: int = len(self.graph[0])
        self.start: tuple[int, int] = (-1, -1)

        for r, row in enumerate(self.graph):
            for c, col in enumerate(row):
                if col == "S":
                    self.start = (r, c)
                    break

    def solve(self) -> int:
        count: int = 0
        beam: set[int] = set()
        beam.add(self.start[1])
        curr_row: int = self.start[0] + 1
        while curr_row < self.max_row:
            for c, val in enumerate(self.graph[curr_row]):
                if val == "^" and c in beam:
                    beam.update({c - 1, c + 1})
                    beam.remove(c)
                    count += 1
            curr_row += 1
        return count


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_path.exists():
        with input_path.open("r") as input_file:
            s = Solution(input_file)
            print(s.solve())
