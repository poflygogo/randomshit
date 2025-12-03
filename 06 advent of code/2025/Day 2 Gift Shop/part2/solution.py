# advent of code 2025
# Day 2: Gift Shop
# Part 2
# python 3.12

import pathlib
from typing import TextIO, Iterable


def get_factors(num: int) -> Iterable[int]:
    return filter(lambda x: num % x == 0, range(1, num))


def solve(input_file: TextIO) -> int:
    result: int = 0
    for lft, rgt in map(lambda x: map(int, x.split("-")), input_file.read().split(",")):
        for num in range(lft, rgt + 1):
            num_str: str = str(num)
            length: int = len(num_str)
            if any(
                num_str == (num_str[:k] * (length // k)) for k in get_factors(length)
            ):
                result += num
    return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r", encoding="utf-8") as input_file:
        print(solve(input_file))
