# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e173. 圍棋入門 - 真眼假眼

direction_side = ((0, 1), (0, -1), (-1, 0), (1, 0))
direction_corner = ((1, 1), (1, -1), (-1, 1), (-1, -1))


def what_eye_is_it(size: int, board: list, col: int, row: int):
    # 如果根本不是空格，那就不用再看了
    if board[row][col] != ".":
        return "Interesting..."

    # 分辨位置
    # 2=在角落, 1=在邊界上但不是角落, 0=其他
    position_type = bool(row in (0, size - 1)) + bool(col in (0, size - 1))

    # 統計相鄰四格的棋子總數
    black = white = 0
    for i, j in direction_side:
        r, c = row + i, col + j
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == "O":
                black += 1
            elif board[r][c] == "X":
                white += 1

    # 判斷是否是眼
    if (
        (position_type == 0 and max(white, black) != 4)
        or (position_type == 1 and max(white, black) != 3)
        or (position_type == 2 and max(white, black) != 2)
    ):
        return "Interesting..."

    # 統計角落四格的棋子總數
    for i, j in direction_corner:
        r, c = row + i, col + j
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == "O":
                black += 1
            elif board[r][c] == "X":
                white += 1

    # 判斷是否是真眼
    if (
        (position_type == 0 and max(white, black) >= 7)
        or (position_type == 1 and max(white, black) == 5)
        or (position_type == 2 and max(white, black) == 3)
    ):
        return "Real!"
    else:
        return "Fake!"


def main():
    n = int(input())
    while n:
        board = [input() for _ in range(n)]
        for _ in range(int(input())):
            a, b = map(int, input().split())
            print(what_eye_is_it(n, board, a - 1, n - b))
        n = int(input())


main()
