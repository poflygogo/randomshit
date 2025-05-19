# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f712. 撲克排序-1


# ---------------------------------------------------

import sys
import io
Q = """
2
26 25 47 10 29 50 12 49 17 41 31 40 19 24 0 27 8 36 23 32 42 30 13 6 15 37 35 39 51 45 28 14 5 18 2 46 4 43 44 11 22 1 9 38 34 7 21 20 3 16 48 33
31 42 40 38 16 14 39 18 49 10 7 1 33 34 36 11 6 5 17 45 25 15 19 46 30 12 29 44 21 13 8 50 9 4 35 20 41 37 27 22 43 48 24 0 26 23 28 3 2 51 47 32
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


from typing import Iterator, List


CARD_SUIT = {0: 'S', 1: 'H', 2: 'D', 3: 'C'}
CARD_NUM = {13: 'A', 1: '2', 2: '3', 3: '4', 4: '5',
            5: '6', 6: '7', 7: '8', 8: '9', 9: 'T',
            10: 'J', 11: 'Q', 12: 'K'}


def custom_sort_rule(arr: List):
    return [arr[i][0] for i in range(1, 6)], arr[1][1]


def ipt_converter(s: str):
    a, b = divmod(int(s), 13)
    if b == 0:
        b = 13
    return (b, a)


def grouper(arr: Iterator, n: int = 10):
    # 一維陣列轉二維
    iterators = [arr] * n
    arr = list(zip(*iterators))
    # 回傳反轉後的二維矩陣
    return [[i] + sorted(j, reverse=True, key=lambda x: (x[0], -x[1])) for i, j in enumerate(zip(*arr), start=1)]


def main():
    for test_case in range(1, int(input()) + 1):
        print(f'Case {test_case}:')
        arr = grouper(map(ipt_converter, input().split()))
        arr.sort(key=custom_sort_rule, reverse=True)
        print('\n'.join(f'{id} {" ".join(CARD_SUIT[j] + CARD_NUM[i] for i, j in card)}' for id, *card in arr))


if __name__ == '__main__':
    main()
