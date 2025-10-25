# python 3.12
# ZeroJudge r489. 2. 航空拍照圖
# APCS 2025-10

from typing import List


def similarity(p1: List[List[int]], p2: List[List[int]]) -> int:
    rows = len(p1)
    cols = len(p1[0])
    if rows != len(p2) or cols != len(p2[0]):
        return 0
    return (
        sum(p1[i][j] == p2[i][j] for i in range(rows) for j in range(cols))
        * 100
        // (rows * cols)
    )


def rotate(arr: List[List[int]]):
    yield arr
    for _ in range(3):
        arr = [list(row) for row in zip(*arr)][::-1]
        yield arr


def main():
    rows, cols = map(int, input().split())
    photo1 = [list(map(int, input().split())) for _ in range(rows)]
    photo2 = [list(map(int, input().split())) for _ in range(rows)]

    print(f"{max(similarity(photo1, i) for i in rotate(photo2))}%")


main()
