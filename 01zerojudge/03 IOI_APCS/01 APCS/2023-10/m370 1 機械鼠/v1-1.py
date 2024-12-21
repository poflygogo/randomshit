# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge m370. 1. 機械鼠
# 2023-10 APCS

# 老鼠會吃他腳下的東西嗎?


from bisect import bisect_left


def main():
    x, n = map(int, input().split())
    foods = sorted(map(int, input().split()))
    idx = bisect_left(foods, x)     # 二分搜，尋找距離老鼠最近的食物位置
    if idx > n // 2:
        print(idx, foods[0])
    else:
        print(n - idx, foods[-1])


main()
