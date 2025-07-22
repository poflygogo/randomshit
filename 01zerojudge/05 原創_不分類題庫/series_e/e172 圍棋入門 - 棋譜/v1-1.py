# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e172. 圍棋入門 - 棋譜


# ---------------------------------------------------

import sys
import io

Q = """
3
4 4
16 4
4 16
8
1 1
1 2
2 1
2 2
3 2
3 1
2 1
1 1
0
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


def make_board():
    return [[0] * 19 for _ in range(19)]


while True:
    n = int(input())
    if n == 0:
        break

    result = make_board()
    dupe = {}
    for i in range(1, n + 1):
        x, y = map(lambda x: int(x) - 1, input().split())
        if result[y][x] == 0:
            result[y][x] = i
        elif result[y][x] in dupe:
            dupe[result[y][x]].append(i)
        else:
            dupe[result[y][x]] = [i]

    print("\n".join(" ".join(map(str, i)) for i in reversed(result)))
    if dupe:
        print("\n".join(f'{i} = ' + ' = '.join(map(str, dupe[i])) for i in sorted(dupe)))

    print()

