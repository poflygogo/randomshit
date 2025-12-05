# advent of code 2024
# day 8 resonant collinearity
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple

from collections import defaultdict


class Point(NamedTuple):
    x: int
    y: int


class Solution:
    def __init__(self, input_file: TextIO):
        self.grid: list[list[str]] = input_file.read().splitlines()
        self.max_row: int = len(self.grid)
        self.max_col: int = len(self.grid[0])

    def solve(self) -> int:
        mark_special_frequency = self.mark_special_frequency()
        antinodes: set[Point] = set()
        for group in mark_special_frequency.values():
            if len(group) == 1:
                continue
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    antinodes.update(self.find_antinode(group[i], group[j], True))
                    antinodes.update(self.find_antinode(group[i], group[j], False))

        return len(antinodes)

    def mark_special_frequency(self) -> defaultdict[str, list[Point]]:
        result: defaultdict[str, list[Point]] = defaultdict(list)
        for row in range(self.max_row):
            for col in range(self.max_col):
                if self.grid[row][col] != ".":
                    result[self.grid[row][col]].append(Point(row, col))
        return result

    def find_antinode(self, p1: Point, p2: Point, mode_add: bool) -> set[Point]:
        vector = Point(p2.x - p1.x, p2.y - p1.y)
        if mode_add is False:
            vector = Point(-vector.x, -vector.y)

        marked: set[Point] = set()
        p = p2 if mode_add else p1  # NOTE: regardless of distance
        while self.is_valid(p):
            marked.add(p)
            p = Point(p.x + vector.x, p.y + vector.y)

        return marked

    def is_valid(self, point: Point) -> bool:
        return 0 <= point.x < self.max_row and 0 <= point.y < self.max_col


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        s = Solution(input_file)
        print(s.solve())
