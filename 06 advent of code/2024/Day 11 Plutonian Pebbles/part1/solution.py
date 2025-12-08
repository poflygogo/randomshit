# advent of code 2024
# Day 11: Plutonian Pebbles
# part 1
# python 3.12

import pathlib
from typing import TextIO
from functools import cache


class Solution:
    def __init__(self, input_file: TextIO) -> None:
        self.arr: list[int] = list(map(int, input_file.read().split()))

    def solve(self, blink_times: int = 25) -> int:
        return sum(self.dfs(i, blink_times) for i in self.arr)

    @cache
    def dfs(self, val: int, blink_times: int) -> int:
        if blink_times == 0:
            return 1
        blink_times -= 1
        cnt: int = 0
        if val == 0:
            cnt += self.dfs(1, blink_times)
        elif (size := len(str(val))) % 2 == 0:
            a, b = divmod(val, 10 ** (size // 2))
            cnt += self.dfs(a, blink_times)
            cnt += self.dfs(b, blink_times)
        else:
            cnt += self.dfs(val * 2024, blink_times)
        return cnt


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    if input_path.exists():
        with input_path.open() as f:
            s = Solution(f)
            print(s.solve())
    else:
        print("can't find the file")
