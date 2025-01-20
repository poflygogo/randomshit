# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge f514. 拼字遊戲 (Spelling)
# 2020-12 TOI 練習賽 新手組


alpha = list(input())
target = input()

result = []
for item in target:
    if item in alpha:
        idx = alpha.index(item)
        alpha[idx] = None
        result.append(idx + 1)
    else:
        result.append('X')

print(*result)
