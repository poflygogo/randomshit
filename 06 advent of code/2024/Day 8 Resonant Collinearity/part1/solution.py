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
                    vector = Point(group[j].x - group[i].x, group[j].y - group[i].y)
                    antinode1 = Point(group[i].x - vector.x, group[i].y - vector.y)
                    antinode2 = Point(group[j].x + vector.x, group[j].y + vector.y)
                    if self.is_valid(antinode1):
                        antinodes.add(antinode1)
                    if self.is_valid(antinode2):
                        antinodes.add(antinode2)
        return len(antinodes)

    def mark_special_frequency(self) -> defaultdict[str, list[Point]]:
        result: defaultdict[str, list[Point]] = defaultdict(list)
        for row in range(self.max_row):
            for col in range(self.max_col):
                if self.grid[row][col] != ".":
                    result[self.grid[row][col]].append(Point(row, col))
        return result

    def is_valid(self, point: Point) -> bool:
        return 0 <= point.x < self.max_row and 0 <= point.y < self.max_col


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        s = Solution(input_file)
        print(s.solve())
