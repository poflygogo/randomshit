# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k848. P2.卡牌評分 (Card)
# 2021-10 TOI 新手同好會


def pattern(args) -> tuple:
    i, score = args
    return sum(score[j] == max_values[j] for j in range(3)), -i


data = [tuple(map(int, input().split())) for _ in range(int(input()))]
max_values = [max(j[i] for j in data) for i in range(3)]
result = max(enumerate(data), key=pattern)
print(result[0] + 1)
