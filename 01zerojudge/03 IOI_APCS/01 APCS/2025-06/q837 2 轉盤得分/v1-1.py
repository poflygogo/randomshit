# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q837. 2. 轉盤得分
# 2025年6月APCS


from typing import Iterable


def spin(m: int, n: int, text: list, rotate: list) -> list:
    text_rotate = []
    for i in range(m):
        idx = rotate[i] % n
        idx *= -1
        text_rotate.append(text[i][idx:] + text[i][:idx])
    return text_rotate


def counter(arr: Iterable) -> int:
    count = {}
    for i in arr:
        count[i] = count.get(i, 0) + 1
    return max(count.values())


def main():
    # m: 字串數量, n: 字串長度, k: 轉動次數
    m, n, k = map(int, input().split())
    text = [input().rstrip() for _ in range(m)]
    score = 0
    for _ in range(k):
        rotate = list(map(int, input().split()))
        text = spin(m, n, text, rotate)
        score += sum(counter(text[j][i] for j in range(m)) for i in range(n))
    print(score)


main()
