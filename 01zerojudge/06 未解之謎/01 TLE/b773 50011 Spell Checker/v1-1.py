# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b773. 50011. Spell Checker

# ---------------------------------------------------

import sys
import io
Q = """
5
case
content
contest
common
onganize
4
cases
common
context
come
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------

from sys import stdin
from collections import Counter
from operator import mul

scan = stdin.readline


def compare(table: dict, target: str) -> str:
    if target in table:
        return f'>{target}'
    target_counter = Counter(target)
    possible = []
    for item in table:
        # 比較字串長度
        if abs(len(item) - len(target)) > 1:
            continue

        # 比較字串的元素統計
        temp = target_counter.copy()
        temp.subtract(table[item])
        for i in tuple(temp.keys()):
            if temp[i] == 0:
                del temp[i]
        if (len(temp) == 1 and tuple(temp.values()) in ((1,), (-1,)) or
            (len(temp) == 2 and mul(*temp.values()) == -1)):
            possible.append(item)

    if possible:
        return f'?{" ".join(possible)}'
    else:
        return f'!{target}'


def make_table(a):
    return (a, Counter(a))


def main():
    table = dict(make_table(scan().rstrip()) for _ in range(int(scan().rstrip())))
    for _ in range(int(scan().rstrip())):
        print(compare(table, scan().rstrip()))


if __name__ == '__main__':
    main()
