# advent of code 2024
# day 2 red-nosed reports part 2
# python 3.12

import pathlib

file_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"


def check_strict(data: list[int]) -> bool:
    """Helper: strict check without removing any level (Part 1 logic)"""
    if len(data) < 2:
        return True

    is_increase = data[1] > data[0]

    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]

        # Check direction consistency
        if (diff > 0) != is_increase:
            return False

        # Check difference magnitude (1 to 3)
        if not (1 <= abs(diff) <= 3):
            return False

    return True


def is_safe(data: list[int]) -> bool:
    """check if the data is safe

    sequence is safe if it is either all increasing or all decreasing
    and the difference between any two adjacent numbers is at most 3

    btw now it can remove a single level from unsafe reports to make it safe
    """
    # 1. Check original
    if check_strict(data):
        return True

    # 2. Problem Dampener: try removing one level
    for i in range(len(data)):
        # Create a new list without the element at index i
        new_data = data[:i] + data[i + 1 :]
        if check_strict(new_data):
            return True

    return False


def solve() -> int:
    res = 0
    with open(file_path, "r") as f:
        for line in f:
            data = list(map(int, line.strip().split()))
            res += is_safe(data)
    return res


if __name__ == "__main__":
    print(solve())
