# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f340. 4.俄羅斯方塊 (Tetris)
# 2020-08 TOI 新手同好會


import math


def tetris(row: int, col: int, command: list, direction: int = 0) -> tuple:
    """
    direction: 0-3, 分別代表下左上右, 預設為 0
    return (end_row, end_col, direction)
    """
    curr_row, curr_col = 0, math.ceil(col / 2) - 1
    for comm in command:
        curr_row += 1
        if comm == '1':
            if curr_col < col - 2 or (curr_col == col - 2 and direction == 1):
                curr_col += 1
        elif comm == '2':
            if curr_col > 1 or (curr_col == 1 and direction == 3):
                curr_col -= 1
        elif comm == '3':
            curr_row = row - (1 if direction == 2 else 2)
        elif comm == '4' and 0 < curr_row < row - 1 and 0 < curr_col < col - 1:
            direction = (direction + 1) % 4
        
        if (curr_row == row - 1) or (curr_row == row - 2 and direction != 2):
            break
        
    return curr_row, curr_col, direction


def print_flush(row: int, col: int, end_row: int, end_col: int, direction: int):
    for r in range(row):
        if r < end_row - 1 or r > end_row + 1:
            print('0' * col)
        elif r == end_row - 1:
            if direction == 0:
                print('0' * col)
            else:
                print('0' * end_col + '1' + '0' * (col - end_col - 1))
        elif r == end_row:
            print(
                '0' * (end_col - (1, 1, 1, 0)[direction]) +
                '1' * (3, 2, 3, 2)[direction] +
                '0' * (col - end_col - (2, 1, 2, 2)[direction])
            )
        elif r == end_row + 1:
            if direction == 2:
                print('0' * col)
            else:
                print('0' * end_col + '1' + '0' * (col - end_col - 1))


def main():
    col, row = map(int, input().split())
    input() # python 用不到，相當於下面的 len(command)
    command = input().split()
    end_row, end_col, direction = tetris(row, col, command)
    print_flush(row, col, end_row, end_col, direction)


if __name__ == '__main__':
    main()
