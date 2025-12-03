# advent of code 2024
# day 1 historian hysteria part 2
# python 3.12

import pathlib
from collections import Counter

file_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"


def solve():
    data1, data2 = [], []
    with open(file_path, "r") as file:
        for line in file:
            a, b = map(int, line.split())
            data1.append(a)
            data2.append(b)

    counter1 = Counter(data1)
    counter2 = Counter(data2)

    return sum(counter2.get(i, 0) * i * j for i, j in counter1.items())


if __name__ == "__main__":
    print(solve())
