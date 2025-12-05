# advent of code 2025
# day 5 cafeteria
# part 2
# python 3.12

import pathlib
from typing import TextIO


class Solution:
    def __init__(self, input_file: TextIO):
        self.fresh_foods: list[tuple[int, int]] = self.parse_range(input_file)

    def solve(self) -> int:
        count: int = 0
        for i, j in self.fresh_foods:
            count += j - i + 1
        return count

    def parse_range(self, input_file: TextIO) -> list[tuple[int, int]]:
        data: list[tuple[int, int]] = []
        for line in input_file:
            if not line.strip():
                break
            a, b = line.strip().split("-")
            data.append((int(a), int(b)))

        data.sort()
        result = [data.pop(0)]
        for i, j in data:
            if i > result[-1][1] + 1:
                result.append((i, j))
            else:
                result[-1] = (result[-1][0], max(result[-1][1], j))

        return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        solution = Solution(input_file)
        print(solution.solve())
