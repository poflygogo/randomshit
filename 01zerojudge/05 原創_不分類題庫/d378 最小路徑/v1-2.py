# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d378. 最小路徑


def minimum_path(row: int, col: int, data: list) -> int:
    for c in range(1, col):
        data[0][c] += data[0][c - 1]
    for r in range(1, row):
        data[r][0] += data[r - 1][0]
    for r in range(1, row):
        for c in range(1, col):
            data[r][c] += min(data[r - 1][c], data[r][c - 1])
    return data[-1][-1]


def main():
    case = 0
    while True:
        try:
            row, col = map(int, input().split())
            data = [list(map(int, input().split())) for _ in range(row)]
        except (EOFError, ValueError):
            break

        case += 1
        print(f'Case #{case} :\n{minimum_path(row, col, data)}')


main()
