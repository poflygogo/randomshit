# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12918 Lucky Thief
# ZeroJudge f447


def mainloop():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(((b - a) + (b - 1)) * a // 2)


mainloop()
