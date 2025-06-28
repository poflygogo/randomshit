# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00587 There's treasure everywhere!
# ZeroJudge c092

from math import sqrt

test_case = 1
info = input().rstrip(".").split(",")
while info[0] != "END":
    x = y = 0
    for i in info:
        if i[-2].isalpha():
            n, d = int(i[:-2]), i[-2:]
        else:
            n, d = int(i[:-1]), i[-1]

        if d == "N":
            y += n
        elif d == "S":
            y -= n
        elif d == "E":
            x += n
        elif d == "W":
            x -= n
        elif d == "NE":
            x += n / sqrt(2)
            y += n / sqrt(2)
        elif d == "NW":
            x -= n / sqrt(2)
            y += n / sqrt(2)
        elif d == "SE":
            x += n / sqrt(2)
            y -= n / sqrt(2)
        elif d == "SW":
            x -= n / sqrt(2)
            y -= n / sqrt(2)

    if test_case > 1:
        print()
    print(
        f"Map #{test_case}",
        f"The treasure is located at ({x:.3f},{y:.3f}).",
        f"The distance to the treasure is {sqrt(x**2 + y**2):.3f}.",
        sep="\n"
    )
    test_case += 1
    info = input().rstrip(".").split(",")
