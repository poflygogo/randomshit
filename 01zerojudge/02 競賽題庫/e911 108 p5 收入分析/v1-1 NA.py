# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e911. 108 p5. 收入分析
# 108新北市資訊學科能力複賽


# ---------------------------------------------------

import sys
import io
Q = """10 1
4 9 5 8 7 5 2 9 3 0
3
3 8 0 0 1 8 0 0 7 9 0 0"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def main():
    x, y = map(int, input().split())
    arr = list(map(int, input().split()))
    n = int(input())
    request = list(map(int, input().split()))

    prefix_sum(arr, x)
    print(*[income(arr, x, *request[i:i + 4]) for i in range(0, len(request), 4)])


def prefix_sum(arr: list, x: int):
    for i in range(1, x):
        arr[i] += arr[i - 1]
    for i in range(x, len(arr), x):
        for j in range(i, i + x):
            arr[j] += arr[j - x]
            if j % x != 0:
                arr[j] += arr[j - 1] - arr[j - x - 1]


def income(arr: list, x: int, x1: int, x2: int, y1: int, y2: int):
    a = y2 * x + x2
    b = y2 * x + x1 - 1
    c = (y1 - 1) * x + x2
    d = (y1 - 1) * x + x1 - 1
    return arr[a] - arr[b] * (x1 > 0) - arr[c] * (y1 > 0) + arr[d] * (x1 > 0 and y1 > 0)


main()
