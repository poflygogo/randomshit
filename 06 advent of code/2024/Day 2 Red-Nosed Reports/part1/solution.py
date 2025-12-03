# advent of code 2024
# day 2 red-nosed reports part 1
# python 3.12

import pathlib

file_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"


def is_safe(data: list[int]) -> bool:
    """check if the data is safe

    sequence is safe if it is either all increasing or all decreasing
    and the difference between any two adjacent numbers is at most 3
    """
    is_increase: bool = data[0] < data[1]
    for i, j in enumerate(range(len(data) - 1), start=1):
        diff = data[i] - data[j]
        if (diff > 0) != is_increase or abs(diff) > 3 or diff == 0:
            return False
    return True


def solve() -> int:
    res = 0
    with open(file_path, "r") as f:
        for line in f:
            data = list(map(int, line.strip().split()))
            res += is_safe(data)
    return res


if __name__ == "__main__":
    print(solve())
