# advent of code 2024
# day 5 print queue
# part 1
# python 3.12

import pathlib
from typing import TextIO

from collections import defaultdict


class NumberInfo:
    def __init__(self):
        self.prev: set[int] = set()
        self.after: set[int] = set()


def read_pattern(input_file: TextIO) -> dict[int, NumberInfo]:
    data: defaultdict[int, NumberInfo] = defaultdict(NumberInfo)
    for line in input_file:
        if not line.strip():
            break
        a, b = map(int, line.strip().split("|"))
        data[a].after.add(b)
        data[b].prev.add(a)
    return data


def is_valid(arr: list[int], pattern: defaultdict[int, NumberInfo]) -> bool:
    length: int = len(arr)
    for idx, val in enumerate(arr):
        if any(arr[i] in pattern[val].prev for i in range(idx + 1, length)):
            return False
        if any(arr[i] in pattern[val].after for i in range(idx)):
            return False
    return True


def solve(input_file: TextIO) -> int:
    pattern: defaultdict[int, NumberInfo] = read_pattern(input_file)
    result: int = 0
    for line in input_file:
        arr: list[int] = list(map(int, line.strip().split(",")))
        if is_valid(arr, pattern):
            result += arr[len(arr) // 2]
    return result


if __name__ == "__main__":
    input_path: TextIO = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open("r") as file:
        print(solve(file))
