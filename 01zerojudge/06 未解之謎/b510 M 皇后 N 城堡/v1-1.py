# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b510. M 皇后 N 城堡


def queen(cnt_queen: int, cnt_castle: int):
    size = cnt_queen + cnt_castle
    dial1 = [0] * (size * 2 - 1)
    dial2 = [0] * (size * 2 - 1)
    horizon = [0] * size
    counter = 0

    def _impl(row: int, queen: int = cnt_queen, castle: int = cnt_castle):
        if row == size:
            nonlocal counter
            counter += 1
            return

        for col in range(size):
            if horizon[col]:
                continue

            if castle > 0 and dial1[row + col] != 1 and dial2[row - col + size - 1] != 1:
                horizon[col] = 2
                dial1[row + col] = 2
                dial2[row - col + size - 1] = 2

                _impl(row + 1, queen, castle - 1)

                horizon[col] = 0
                dial1[row + col] = 0
                dial2[row - col + size - 1] = 0

            if queen > 0 and dial1[row + col] == 0 and dial2[row - col + size - 1] == 0:
                horizon[col] = 1
                dial1[row + col] = 1
                dial2[row - col + size - 1] = 1

                _impl(row + 1, queen - 1, castle)

                horizon[col] = 0
                dial1[row + col] = 0
                dial2[row - col + size - 1] = 0

    _impl(0)
    return counter


def main():
    while True:
        try:
            m, n = map(int, input().split())
            print(queen(m, n))
        except EOFError:
            break


main()
