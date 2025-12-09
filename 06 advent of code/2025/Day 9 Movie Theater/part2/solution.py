# advent of code 2025
# Day 9: Movie Theater
# part 1
# python 3.12

import pathlib
from typing import TextIO, NamedTuple
from itertools import combinations
from enum import Enum
from collections import deque
from copy import deepcopy


class Point(NamedTuple):
    row: int
    col: int

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.row + other.row, self.col + other.col)


class Direction(Enum):
    UP = Point(-1, 0)
    DOWN = Point(1, 0)
    LEFT = Point(0, -1)
    RIGHT = Point(0, 1)


class Color(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    OUTER = 3  # mark as outer :P


class Solution:
    def __init__(self, input_file: TextIO):
        self.input_file: TextIO = input_file
        self.all_points: list[Point] = []  # 不僅是紀錄所有座標，也記錄了座標順序
        self.rows: list[int]
        self.cols: list[int]
        self.r_to_idx: dict[int, int]
        self.c_to_idx: dict[int, int]
        self.compress_grid: list[list[Color]]

    def solve(self) -> int:
        self.initialize_grid()
        self.mark_red_tile()
        self.draw_edges()
        self.fill_grid()

        max_size: int = 0
        for p1, p2 in combinations(self.all_points, 2):
            if not self.is_valid_square(p1, p2):
                continue
            size = (abs(p1.row - p2.row) + 1) * (abs(p1.col - p2.col) + 1)
            max_size = max(max_size, size)

        return max_size

    def initialize_grid(self):
        # 建立稀疏表
        rows: set[int] = set()
        cols: set[int] = set()
        for line in self.input_file:
            col, row = map(int, line.strip().split(","))
            self.all_points.append(Point(row, col))
            rows.update({row, row + 1})
            cols.update({col, col + 1})
        self.rows = sorted(rows)
        self.cols = sorted(cols)

    def mark_red_tile(self):
        self.compress_grid = [
            [Color.NONE] * len(self.cols) for _ in range(len(self.rows))
        ]
        for p in self.all_points:
            self.compress_grid[self.rows.index(p.row)][self.cols.index(p.col)] = (
                Color.RED
            )

    def draw_edges(self):
        # 繪製邊緣
        self.r_to_idx = {real_r: index for index, real_r in enumerate(self.rows)}
        self.c_to_idx = {real_c: index for index, real_c in enumerate(self.cols)}
        for i in range(len(self.all_points)):
            p1, p2 = self.all_points[i - 1], self.all_points[i]
            if p1.row == p2.row:
                ir = self.r_to_idx[p1.row]
                ic1 = self.c_to_idx[p1.col]
                ic2 = self.c_to_idx[p2.col]
                for j in range(min(ic1, ic2) + 1, max(ic1, ic2)):
                    self.compress_grid[ir][j] = Color.GREEN
            else:
                ic = self.c_to_idx[p1.col]
                ir1 = self.r_to_idx[p1.row]
                ir2 = self.r_to_idx[p2.row]
                for j in range(min(ir1, ir2) + 1, max(ir1, ir2)):
                    self.compress_grid[j][ic] = Color.GREEN

    def fill_grid(self):
        # 填充綠色的空間
        # 但因為不知道哪邊是裡面，所以先從外面開始填(至少這個可以很肯定)
        # 建表時記得要開大一點，至少要比原本的大一格(確保最外圈一定是相連的)
        grid: list[list[Color]] = deepcopy(self.compress_grid)
        for row in grid:
            row.insert(0, Color.NONE)
        grid.insert(0, [Color.NONE] * len(grid[0]))

        max_row: int = len(grid)
        max_col: int = len(grid[0])

        # 使用 bfs 有助於避免 dfs 的 stack overflow 風險
        start: Point = Point(0, 0)
        grid[start.row][start.col] = Color.OUTER
        queue: deque[Point] = deque([start])
        while queue:
            p = queue.popleft()
            for np in map(lambda x: x.value + p, Direction):
                if not (0 <= np.row < max_row and 0 <= np.col < max_col):
                    continue
                if grid[np.row][np.col] != Color.NONE:
                    continue
                grid[np.row][np.col] = Color.OUTER
                queue.append(np)

        # 確認那些在外面的點後，剩下沒有著色的就都是在裡面的點了
        for r in range(1, max_row):
            for c in range(1, max_col):
                if grid[r][c] == Color.NONE:
                    self.compress_grid[r - 1][c - 1] = Color.GREEN

    def is_valid_square(self, p1: Point, p2: Point) -> bool:
        # 整理成左上-右下的形式
        min_p: Point = Point(min(p1.row, p2.row), min(p1.col, p2.col))
        max_p: Point = Point(max(p1.row, p2.row), max(p1.col, p2.col))

        ir_start: int = self.r_to_idx[min_p.row]
        ic_start: int = self.c_to_idx[min_p.col]
        ir_end: int = self.r_to_idx[max_p.row]
        ic_end: int = self.c_to_idx[max_p.col]

        for r in range(ir_start, ir_end):
            for c in range(ic_start, ic_end):
                if self.compress_grid[r][c] == Color.NONE:
                    return False
        return True

    def debug_print_graph(self, grid: list[list[Color]]):
        import logging

        log_file_name: str = "check.log"

        # clear previous log
        log_file_path = pathlib.Path(__file__).parent / log_file_name
        if log_file_path.exists():
            with log_file_path.open("w") as f:
                f.write("")

        logging.basicConfig(
            level=logging.DEBUG,
            filename=log_file_name,
            filemode="a",
        )

        for row in grid:
            lst = [".#Xo"[i.value] for i in row]
            logging.debug("".join(lst))


if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_file.exists():
        with input_file.open() as f:
            s = Solution(f)
            print(s.solve())
    else:
        print("file no found")
