# advent of code 2024
# Day 3: Mull It Over
# part 1
# python 3.12

import pathlib
from typing import TextIO

from re import finditer
from operator import mul


def solve(input_file: TextIO) -> int:
    pattern1 = r"mul\(\d+,\d+\)"
    pattern2 = r"\d+"
    result = 0
    for expr in finditer(pattern1, input_file.read()):
        result += mul(*map(lambda x: int(x.group()), finditer(pattern2, expr.group())))
    return result


if __name__ == "__main__":
    input_file = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_file, "r", encoding="utf-8") as file:
        print(solve(file))
