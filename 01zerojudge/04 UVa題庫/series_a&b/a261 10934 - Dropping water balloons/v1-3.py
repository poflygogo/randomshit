# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10934 Dropping water balloons
# ZeroJudge a261


from bisect import bisect_left
from sys import stdin


def make_table(max_balloon: int=100, max_try: int=63):
    dp = [[0 for _ in range(max_try + 1)] for _ in range(max_balloon + 1)]
    for i in range(1, max_balloon + 1):
        for j in range(1, max_try + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1
    return dp


def find_ans(data: str):
    k, n = map(int, data.split())
    if k == 0:
        return ''
    t = bisect_left(dp[k], n)
    if t < 64 and dp[k][t] >= n:
        return str(t)
    return "More than 63 trials needed."


dp = make_table()
print('\n'.join(map(find_ans, stdin)))
