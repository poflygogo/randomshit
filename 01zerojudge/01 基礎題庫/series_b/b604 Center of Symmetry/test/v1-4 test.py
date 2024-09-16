# from sys import stdin
from math import ceil


def check_center(le: int, data: list) -> bool:
    data.sort()
    middle = (data[0] + data[-1]) / 2
    for i in range(1, ceil(le / 2)):
        if middle != (data[i] + data[-i - 1]) / 2:
            return False
    return True


stdin = open('test.txt')
for length in stdin:
    length = int(length)
    if not length: break

    arr_x, arr_y = [], []
    for _ in range(length):
        a, b = map(int, stdin.readline().strip().split())
        arr_x.append(a)
        arr_y.append(b)

    if check_center(length, arr_x) and check_center(length, arr_y):
        print('yes')
    else:
        print('no')
