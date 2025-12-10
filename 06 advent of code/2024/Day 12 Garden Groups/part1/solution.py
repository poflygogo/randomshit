# advent of code 2025
# Day 12 Garden Groups
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple
from enum import Enum
from collections import deque


class Point(NamedTuple):
    row: int
    col: int

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.row + other.row, self.col + other.col)


class Directions(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    RIGHT = Point(0, 1)
    LEFT = Point(0, -1)


class Solution:
    def __init__(self, input_file: TextIO):
        self.graph: list[str] = input_file.read().split()
        self.graph_row: int = len(self.graph)
        self.graph_col: int = len(self.graph[0])
        self.visited: list[list[bool]] = [
            [False] * self.graph_col for _ in range(self.graph_row)
        ]

    def solve(self) -> int:
        result: int = 0
        for r in range(self.graph_row):
            for c in range(self.graph_col):
                if self.visited[r][c] is False:
                    result += self.calc_price(Point(r, c))
        return result

    def calc_price(self, start_point: Point) -> int:
        area_label: str = self.graph[start_point.row][start_point.col]

        # (bfs) record the area
        seen: set[Point] = {start_point}
        queue: deque[Point] = deque([start_point])
        while queue:
            p = queue.popleft()
            for np in map(lambda x: x.value + p, Directions):
                if np in seen:
                    continue
                if not self.is_valid_coordinate(np):
                    continue
                if self.graph[np.row][np.col] != area_label:
                    continue
                seen.add(np)
                queue.append(np)

        area_size: int = len(seen)

        # calc the perimeter
        perimeter: int = 0
        for p in seen:
            perimeter += sum(
                i not in seen for i in map(lambda x: x.value + p, Directions)
            )
            # update curr area info to self.visited
            self.visited[p.row][p.col] = True

        return area_size * perimeter

    def is_valid_coordinate(self, p: Point) -> bool:
        return 0 <= p.row < self.graph_row and 0 <= p.col < self.graph_col


if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_file.exists():
        with input_file.open() as f:
            s = Solution(f)
            print(s.solve())
    else:
        print("file no found")
