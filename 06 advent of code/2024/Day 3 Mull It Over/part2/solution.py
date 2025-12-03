# advent of code 2024
# Day 3: Mull It Over
# part 1
# python 3.12

import pathlib
from typing import TextIO

from re import finditer
from operator import mul


def solve(input_file: TextIO) -> int:
    pattern1 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    pattern2 = r"\d+"
    result = 0
    mul_enabled = True
    for expr in finditer(pattern1, input_file.read()):
        if expr.group() == "do()":
            mul_enabled = True
        elif expr.group() == "don't()":
            mul_enabled = False
        elif mul_enabled:  # and expr.group().startswith("mul")
            result += mul(
                *map(lambda x: int(x.group()), finditer(pattern2, expr.group()))
            )
    return result


if __name__ == "__main__":
    input_file: TextIO = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with open(input_file, "r", encoding="utf-8") as file:
        print(solve(file))
