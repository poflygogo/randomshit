# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q889. 快樂學幾何3


from sys import stdin


def calc(a: int, b: int, c: int, d: int) -> int:
    return c - b + a - d


print('\n'.join(map(lambda x: str(calc(*map(int, x.split()))), stdin.read().splitlines())))
