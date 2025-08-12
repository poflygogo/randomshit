# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d534. 1. 戰艦謎題
# 98學年度北基區資訊學科能力競賽


def warship(r1: int, r2: int, c1: int, c2: int) -> str:
    if not (r1 + r2 == c1 + c2 == 6):
        return "No solutions."

    # r1  a  b
    # r2  c  d
    #     c1 c2
    for a in range(4):
        b = r1 - a
        if b > 3:
            continue
        c = c1 - a
        if c < 0 or c > 3:
            continue
        d = c2 - b
        if d < 0 or d > 3:
            continue
        if c + d == r2:
            return f"{a} {b}\n{c} {d}"

    return "No solutions."


print(warship(*map(int, input().split())))

# ------Testing------
# assert warship(5, 1, 4, 2) == "3 2\n1 0", f"{warship(5, 2, 4, 2)}"
# assert warship(3, 3, 1, 5) == "0 3\n1 2", f"{warship(3, 3, 1, 5)}"  # "1 2\n0 3"
# assert warship(3, 2, 3, 4) == "No solutions.", f"{warship(3, 2, 3, 4)}"

# assert warship(1, 5, 2, 4) == "0 1\n2 3", f"{warship(1, 5, 2, 4)}"
# assert warship(4, 2, 5, 1) == "3 1\n2 0", f"{warship(4, 2, 5, 1)}"
# assert warship(4, 3, 5, 2) == "No solutions.", f"{warship(4, 3, 5, 2)}"
# assert warship(5, 1, 2, 4) == "2 3\n0 1", f"{warship(5, 1, 2, 4)}"
# assert warship(2, 4, 5, 1) == "2 0\n3 1", f"{warship(2, 4, 5, 1)}"

# print("fin")
