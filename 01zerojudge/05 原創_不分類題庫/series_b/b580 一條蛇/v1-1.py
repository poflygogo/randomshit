# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b580. 一條蛇


def snake(n: int):
    arr = [[0] * n for _ in range(n)]
    row = col = n // 2
    d = 0   # [0, 1, 2, 3] 下 右 上 左
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    arr[row][col] = 1
    for i in range(2, n * n + 1):
        if ((d == 0 and arr[row][col + 1] == 0) or
            (d == 1 and arr[row - 1][col] == 0) or
            (d == 2 and arr[row][col - 1] == 0) or
            (d == 3 and arr[row + 1][col] == 0)):
            d = (d + 1) % 4
        row += dr[d]
        col += dc[d]
        arr[row][col] = i
    return arr


def main():
    for _ in range(int(input())):
        result = snake(int(input()))
        print('\n'.join(' '.join(str(j).rjust(4) for j in i) for i in result))


main()
