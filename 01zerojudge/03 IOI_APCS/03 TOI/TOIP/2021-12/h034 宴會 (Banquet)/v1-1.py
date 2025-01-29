# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h034. 宴會 (Banquet)
# 2021-12 TOI 練習賽 新手組


n = int(input())
data = [input() for _ in range(n)]
result = []

for i in range(max(len(i) for i in data)):
    for j in range(n):
        if i < len(data[j]) and data[j][i].isalpha():
            result.append(data[j][i])

print(''.join(result))
