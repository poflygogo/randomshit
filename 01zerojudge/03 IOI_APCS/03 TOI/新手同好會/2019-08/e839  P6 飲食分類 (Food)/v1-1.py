# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e839 P6 飲食分類 (Food)
# 2019-08 TOI 新手同好會


data = {}
for _ in range(int(input())):
    food, category = input().split()
    if category not in data:
        data[category] = []
    data[category].append(food)

print(*sorted(data.get(input(), ['No'])), sep='\n')
