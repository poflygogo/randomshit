# advent of code 2025
# day 3 Lobby
# part 2
# python 3.12

import pathlib
from typing import TextIO


def find_max_joltage(digits: list[int]) -> int:
    # greedily find the maximum digit
    res: list[int] = []
    curr: int = 0
    end: int = len(digits) - 11
    while len(res) < 12 and curr < end:
        next_max_digit: int = max(digits[curr:end])
        idx: int = digits.index(next_max_digit, curr)
        res.append(next_max_digit)
        curr = idx + 1
        end += 1
    return int("".join(map(str, res)))


def solve(input_file: TextIO) -> int:
    result: int = 0
    for line in input_file:
        result += find_max_joltage(list(map(int, line.strip())))
    return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        print(solve(input_file))
