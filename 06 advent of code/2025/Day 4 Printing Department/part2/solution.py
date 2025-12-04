# advent of code 2025
# day 4 printing department
# part 2
# python 3.12

import pathlib
from typing import TextIO


class Solution:
    """I just want to avoid global variables"""

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

    def __init__(self, input_file: TextIO):
        self.graph: list[list[str]] = [list(i) for i in input_file.read().splitlines()]
        self.max_row: int = len(self.graph)
        self.max_col: int = len(self.graph[0])

    def solve(self) -> int:
        """calculate the maximum number of paper roll that can be removed"""
        result: int = 0
        to_remove: set[tuple[int, int]] = set()
        while True:
            # find the paper roll that can be removed
            for row in range(self.max_row):
                for col in range(self.max_col):
                    if self.is_removeable(row, col):
                        to_remove.add((row, col))

            # end the loop if no paper roll can be removed
            if len(to_remove) == 0:
                break

            # update the result
            result += len(to_remove)

            # remove the paper roll
            for r, c in to_remove:
                self.graph[r][c] = "x"
            to_remove.clear()

        return result

    def is_removeable(self, row: int, col: int) -> bool:
        """check if the paper roll is removeable"""
        if self.graph[row][col] != "@":
            return False
        cnt: int = 0
        for dr, dc in self.DIRECTIONS:
            nr: int = row + dr
            nc: int = col + dc
            if not (0 <= nr < self.max_row and 0 <= nc < self.max_col):
                continue
            if self.graph[nr][nc] == "@":
                cnt += 1
        return cnt < 4  # return true if near by is less than 4

    def print_graph(self):
        """print the graph(for debug)"""
        for row in self.graph:
            print("".join(row))


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        s = Solution(input_file)
        print(s.solve())
