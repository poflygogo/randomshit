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
from collections import OrderedDict

scan = stdin.readline


def compare(table: dict, target: str) -> str:
    if target in table:
        return f'>{target}'
    possible = []
    for item in table:
        # 比較字串長度
        if abs(table[item] - len(target)) > 1:
            continue

        # 比較字串的元素統計
        if compare_each_char(item, target):
            possible.append(item)

    if possible:
        return f'?{" ".join(possible)}'
    else:
        return f'!{target}'


def compare_each_char(a: str, b: str) -> bool:
    if len(a) == len(b):
        return sum(i != j for i, j in zip(a, b)) <= 1
    
    if len(a) < len(b):
        a, b = b, a
    j = 0
    flag = False
    for i in range(len(a)):
        if j < len(b):
            if a[i] == b[j]:
                j += 1
            elif flag:
                return False
            else:
                flag = True
    return True


def make_table(a: str):
    return (a, len(a))


def main():
    table = OrderedDict(make_table(scan().rstrip()) for _ in range(int(scan().rstrip())))
    for _ in range(int(scan().rstrip())):
        print(compare(table, scan().rstrip()))


if __name__ == '__main__':
    main()
