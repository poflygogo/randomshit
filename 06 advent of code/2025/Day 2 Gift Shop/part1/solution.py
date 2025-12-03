# advent of code 2025
# Day 2: Gift Shop
# Part 1
# python 3.12

import pathlib
from typing import TextIO


def solve(input_file: TextIO) -> int:
    result: int = 0
    for i, j in map(lambda x: map(int, x.split("-")), input_file.read().split(",")):
        for num in range(i, j + 1):
            num_str: str = str(num)
            if len(num_str) % 2 != 0:
                continue
            if num_str[: len(num_str) // 2] == num_str[len(num_str) // 2 :]:
                result += num

    return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r", encoding="utf-8") as input_file:
        print(solve(input_file))
