# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a700. 2、国王的麦子(Wheat)


def mainloop():
    while True:
        try:
            i, j = map(int, input().split())
        except EOFError:
            break
        else:
            print(king_wheat(i, j))


def king_wheat(i: int, j: int) -> int:
    return 2 ** (8 * (i - 1) + j - 1)


mainloop()
