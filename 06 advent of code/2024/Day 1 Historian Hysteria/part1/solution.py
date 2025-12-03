# advent of code 2024
# day 1 historian hysteria part 1
# python 3.12

import pathlib

file_path = pathlib.Path(__file__).parent.parent / "test_case" / "00.in"

def solve():
    data1, data2 = [], []
    with open(file_path, "r") as file:
        for line in file:
            a, b = map(int, line.split())
            data1.append(a)
            data2.append(b)
    
    data1.sort()
    data2.sort()

    return sum(abs(a - b) for a, b in zip(data1, data2))


if __name__ == "__main__":
    print(solve())
