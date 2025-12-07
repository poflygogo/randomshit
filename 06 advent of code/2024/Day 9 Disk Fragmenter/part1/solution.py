# advent of code 2024
# day 9 disk fragmenter
# part 1
# python 3.12

import pathlib
from typing import TextIO, Iterator


class Solution:
    def __init__(self, input_file: TextIO):
        self.disk_map: Iterator[int] = map(int, input_file.read().strip())

    def solve(self) -> int:
        data: list[int | None] = []
        flag: bool = True
        val: int = 0
        for i in self.disk_map:
            if flag:
                data.extend([val] * i)
                val += 1
            else:
                data.extend([None] * i)
            flag = not flag

        def rindex(data: list[int | None], end: int) -> int:
            while data[end] is None:
                end -= 1
            return end

        lft: int = data.index(None)
        rgt: int = rindex(data, len(data) - 1)

        while lft < rgt:
            data[lft], data[rgt] = data[rgt], data[lft]
            lft = data.index(None, lft + 1)
            rgt = rindex(data, rgt - 1)

        return sum(i * v for i, v in enumerate(data) if v is not None)


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open() as input_file:
        s = Solution(input_file)
        print(s.solve())
