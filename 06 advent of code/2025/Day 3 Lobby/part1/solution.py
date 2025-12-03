# advent of code 2025
# day 3 Lobby
# part 1
# python 3.12

import pathlib
from typing import TextIO

from itertools import combinations as comb


def find_max_joltage(digits: str) -> int:
    # I'm lazy... bruteforce...
    return max(int(i + j) for i, j in comb(digits, 2))  # take 2 digits at a time


def solve(input_file: TextIO) -> int:
    result: int = 0
    for line in input_file:
        result += find_max_joltage(line.strip())
    return result


if __name__ == "__main__":
    input_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_path, "r") as input_file:
        print(solve(input_file))
