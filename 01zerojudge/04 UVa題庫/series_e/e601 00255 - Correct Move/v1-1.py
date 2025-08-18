# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00255 - Correct Move
# ZeroJudge e601


def judge(king: int, queen: int, queen_next: int) -> str:
    def jump(a: int, b: int, c: int):
        return (a <= b <= c) or (c <= b <= a)

    # 不用檢查 king 和 queen 是否介於 0 到 63 之間
    # 否則會在 zerojudge 吃 WA
    if king == queen:
        return "Illegal state"

    if (king, queen_next) in ((0, 9), (56, 49), (7, 14), (63, 54)):
        return "Stop"

    king_x, king_y = divmod(king, 8)
    queen_x, queen_y = divmod(queen, 8)
    queen_next_x, queen_next_y = divmod(queen_next, 8)

    if (
        (queen_x != queen_next_x and queen_y != queen_next_y)
        or (queen == queen_next)
        or (queen_x == queen_next_x == king_x and jump(queen_y, king_y, queen_next_y))
        or (queen_y == queen_next_y == king_y and jump(queen_x, king_x, queen_next_x))
    ):
        return "Illegal move"

    if (
        (king_x == queen_next_x and abs(queen_next_y - king_y) < 2)
        or (king_y == queen_next_y and abs(queen_next_x - king_x) < 2)
    ):
        return "Move not allowed"

    return "Continue"


def main():
    while True:
        try:
            print(judge(*map(int, input().split())))
        except EOFError:
            break


if __name__ == "__main__":
    main()
