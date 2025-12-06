# advent of code 2025
# day 6 Trash Compactor
# part 2
# python 3.12

import pathlib
from typing import TextIO


import math
from itertools import zip_longest


class Solution:
    def __init__(self, input_file: TextIO):
        self.input_file = input_file

    def solve(self) -> int:
        nums_line: list[str] = self.input_file.read().splitlines()
        operators: list[str] = nums_line.pop().split()
        operators_iter = iter(operators)

        result: int = 0
        tmp: list[int] = []
        for digits in zip_longest(*nums_line, fillvalue=" "):
            num_str = "".join(digits).strip()
            if num_str:
                tmp.append(int(num_str))
            else:
                result += self.calculate(tmp, next(operators_iter))
                tmp.clear()

        if tmp:
            result += self.calculate(tmp, next(operators_iter))

        return result

    def calculate(self, nums: list[int], operator: str) -> int:
        if operator == "+":
            return sum(nums)
        elif operator == "*":
            return math.prod(nums)


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        solution = Solution(input_file)
        print(solution.solve())
