# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12869 Zeroes
# ZeroJudge g470


def fzero(n: int) -> int:
    """ 計算數字結尾 0 的數量，只需要判斷有幾個 5 即可
    """
    if n < 5:
        return 0
    n //= 5
    return n + fzero(n)


a, b = map(int, input().split())
while not (a == b == 0):
    print(len({fzero(i) for i in range(a, b + 1)}))
    a, b = map(int, input().split())
