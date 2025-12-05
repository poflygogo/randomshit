# advent of code 2024
# day 7 bridge repair
# part 2
# python 3.12

import pathlib
from typing import TextIO, Callable
from dataclasses import dataclass


class Solution:
    @dataclass
    class Expr:
        target: int
        nums: list[int]

    operator: dict[str, Callable[[int, int], int]] = {
        "+": lambda x, y: x + y,
        "*": lambda x, y: x * y,
        "||": lambda x, y: int(str(x) + str(y)),
    }

    def __init__(self, input_file: TextIO):
        self.input_file: TextIO = input_file

    def solve(self) -> int:
        result: int = 0
        for line in self.input_file:
            expr: self.Expr = self.read_expr(line)
            if self.is_possible(expr, expr.nums[0]):
                result += expr.target
        return result

    def read_expr(self, line: str) -> Expr:
        # maybe make it as generator is better?
        target, nums = line.strip().split(":")
        return self.Expr(int(target), list(map(int, nums.strip().split())))

    @staticmethod
    def is_possible(expr: Expr, curr_val: int, idx: int = 1) -> bool:
        """Check if the expression is possible.

        DFS(backtracking)
        use idx to track the current index of the expression.
        """
        if idx >= len(expr.nums):
            return expr.target == curr_val
        for func in Solution.operator.values():
            res: int = func(curr_val, expr.nums[idx])
            if Solution.is_possible(expr, res, idx + 1):
                return True
        return False


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        s = Solution(input_file)
        print(s.solve())
