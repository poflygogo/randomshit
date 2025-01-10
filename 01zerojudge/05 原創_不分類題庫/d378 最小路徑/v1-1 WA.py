# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d378. 最小路徑


def minimum_path(row: int, col: int, data: list) -> int:
    dp = [[0] * (col + 1) for _ in range(row + 1)]
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            dp[r][c] = min(dp[r -1][c], dp[r][c - 1]) + data[r - 1][c - 1]
    return dp[-1][-1]


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
