# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e174. 圍棋基礎 - 整地

# 挺沒必要的，但就是想這樣寫哈哈
from enum import Enum

SIZE = 19
DIRECTION = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Player(Enum):
    black = "Black"
    white = "White"
    default = "None"


class GameResult:
    black: int = 0
    white: int = 0
    winner: Player = Player.default

    def __str__(self) -> str:
        if self.black > self.white:
            self.winner = Player.black
        else:
            self.winner = Player.white
        return f"O:{self.black}\nX:{self.white}\n{self.winner.value} win!!"


def calc_the_score(board: list):
    seen = set()
    result = GameResult()
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == "O":
                result.black += 1
            elif board[r][c] == "X":
                result.white += 1
            elif (r, c) not in seen:
                count_area(board, seen, result, r, c)
    return result


def count_area(board: list, seen: set, result: GameResult, row: int, col: int):
    cnt = 0
    team = Player.default
    queue = [(row, col)]
    while queue:
        r, c = queue.pop(0)
        if not (0 <= r < SIZE and 0 <= c < SIZE) or (r, c) in seen:
            continue

        if board[r][c] == ".":
            cnt += 1
            seen.add((r, c))
            queue.extend([(r + i, c + j) for i, j in DIRECTION])
        elif board[r][c] == "O":
            team = Player.black
        else:
            team = Player.white

    if team == Player.black:
        result.black += cnt
    else:
        result.white += cnt


def main():
    for _ in range(int(input())):
        print(calc_the_score([input() for _ in range(SIZE)]))


main()
