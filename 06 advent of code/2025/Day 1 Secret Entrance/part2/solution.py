# Advent of Code 2025
# Day 1 - Secret Entrance
# Part 2
# python 3.12

import pathlib
from typing import TextIO


def solve(input_file: TextIO) -> int:
    curr_pos: int = 50
    count: int = 0
    for line in input_file:
        line = line.strip()
        direction, distance = line[0], int(line[1:])

        # calculate the number of multiples of 100 
        # in the half-open interval [old_pos, curr_pos)
        old_pos = curr_pos
        if direction == "R":
            curr_pos += distance
            count += curr_pos // 100
        elif direction == "L":
            curr_pos -= distance
            count += (old_pos - 1) // 100 - (curr_pos - 1) // 100
        curr_pos %= 100
    return count


if __name__ == "__main__":
    file_path: pathlib.Path = (
        pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    )
    with file_path.open("r", encoding="utf-8") as file:
        print(solve(file))
