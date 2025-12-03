# Advent of Code 2025
# Day 1 - Secret Entrance
# Part 1
# python 3.12

import pathlib
from typing import TextIO


def solve(input_file: TextIO) -> int:
    curr_pos: int = 50
    count: int = 0
    for line in input_file:
        line = line.strip()
        direction, distance = line[0], int(line[1:])
        match direction:
            case "L":
                curr_pos -= distance
            case "R":
                curr_pos += distance
        curr_pos %= 100
        if curr_pos == 0:
            count += 1
    return count


if __name__ == "__main__":
    file_path: pathlib.Path = (
        pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    )
    with file_path.open("r", encoding="utf-8") as file:
        print(solve(file))
