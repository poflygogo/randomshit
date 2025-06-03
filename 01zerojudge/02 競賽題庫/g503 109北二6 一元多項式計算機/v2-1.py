# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g503. 109北二6.一元多項式計算機
# 109北二區桃竹苗資訊學科能力複賽


# ---------------------------------------------------

import sys
import io
Q = """4 2 3
-1 5
-1 3
1 6
1 4"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



def num_slicer(num: int, limit: int) -> int:
    sign = num < 0
    if sign:
        num = abs(num)
    num_str = str(num)
    num_str = num_str[::-1][:limit][::-1]
    if sign:
        return -int(num_str)
    else:
        return int(num_str)


def main():
    n, c, m = map(int, input().split())
    result = 0
    for _ in range(n):
        a, b = map(int, input().split())
        result = num_slicer(result + num_slicer(num_slicer(a, m) * num_slicer(num_slicer(c, m) ** b, m), m), m)
    print(str(result).lstrip('-').zfill(m))


main()
