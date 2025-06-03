# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10934 Dropping water balloons
# ZeroJudge a261


def main():
    dp = make_table()
    while True:
        k, n = map(int, input().split())
        if k == 0:
            break
        print(find_ans(dp, k, n))


def make_table(max_balloon: int=100, max_try: int=63):
    dp = [[0 for _ in range(max_try + 1)] for _ in range(max_balloon + 1)]
    for i in range(1, max_balloon + 1):
        for j in range(1, max_try + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + 1
    return dp


def find_ans(dp: list, k: int, n: int):
    for t in range(1, 64):
        if dp[k][t] >= n:
            return t
    return "More than 63 trials needed."


main()
