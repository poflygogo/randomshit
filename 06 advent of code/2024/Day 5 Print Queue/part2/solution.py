# advent of code 2024
# day 5 print queue
# part 1
# python 3.12

import pathlib
from typing import TextIO

from collections import defaultdict
from functools import cmp_to_key


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


def is_valid(arr: list[int], pattern: defaultdict[int, NumberInfo]) -> tuple[bool, int]:
    """check if the array is valid

    return True if valid, else return the index of the first invalid number(might be the only too?)
    """
    length: int = len(arr)
    for idx, val in enumerate(arr):
        for i in range(idx + 1, length):
            if arr[i] in pattern[val].prev:
                return False, idx
        for i in range(idx):
            if arr[i] in pattern[val].after:
                return False, idx
    return True, -1  # just to make mypy happy


def solve(input_file: TextIO) -> int:
    pattern: defaultdict[int, NumberInfo] = read_pattern(input_file)
    result: int = 0

    for line in input_file:
        arr: list[int] = list(map(int, line.strip().split(",")))
        flag, idx = is_valid(arr, pattern)
        if flag:
            continue

        # sort using custom comparator
        def compare(a: int, b: int) -> int:
            if b in pattern[a].after:
                return -1
            if b in pattern[a].prev:
                return 1
            return 0

        arr.sort(key=cmp_to_key(compare))

        result += arr[len(arr) // 2]
    return result


if __name__ == "__main__":
    input_path: TextIO = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"
    with input_path.open("r") as file:
        print(solve(file))
