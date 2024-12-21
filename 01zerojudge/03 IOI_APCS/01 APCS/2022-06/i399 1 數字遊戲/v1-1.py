# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i399. 1. 數字遊戲
# 2022-06 APCS


nums = list(map(int, input().split()))
counter = {}
for i in nums:
    counter[i] = counter.get(i, 0) + 1

print(max(counter.values()), *sorted(counter, reverse=True))
