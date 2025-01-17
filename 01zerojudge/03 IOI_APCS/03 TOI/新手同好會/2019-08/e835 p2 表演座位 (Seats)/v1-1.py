# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e835 p2.表演座位 (Seats)
# 2019-08 TOI 新手同好會


def seats(n: int) -> tuple:
    if n <= 2500:
        row, col = divmod(n, 25)
        return 1, row + (col != 0), col if col != 0 else 25
    if n <= 7500:
        n -= 2500
        row, col = divmod(n, 50)
        return 2, row + (col != 0), col if col != 0 else 50
    if n <= 10000:
        n -= 7500
        row, col = divmod(n, 25)
        return 3, row + (col != 0), col if col != 0 else 25


if __name__ == '__main__':
    print(*seats(int(input())))
    nums = [25, 26, 7499, 8765]
    for num in nums:
        print(*seats(num))
