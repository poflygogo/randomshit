# advent of code 2025
# day 6 Trash Compactor
# part 1
# python 3.12

import pathlib
from typing import TextIO


import math


class Solution:
    def __init__(self, input_file: TextIO):
        self.nums, self.operators = self.parse_input(input_file)

    def solve(self) -> int:
        return sum(
            self.calc(nums, op) for nums, op in zip(zip(*self.nums), self.operators)
        )

    def calc(self, nums: list[int], op: str) -> int:
        if op == "+":
            return sum(nums)
        elif op == "*":
            return math.prod(nums)

    def parse_input(self, input_file: TextIO) -> tuple[list[list[int]], list[str]]:
        nums: list[list[int]] = []
        operators: list[str] = []
        for line in input_file:
            line = line.strip().split()
            if not line:
                continue
            if any(x.isdigit() for x in line):
                nums.append([int(x) for x in line])
            else:
                operators = line
        return nums, operators


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        solution = Solution(input_file)
        print(solution.solve())
