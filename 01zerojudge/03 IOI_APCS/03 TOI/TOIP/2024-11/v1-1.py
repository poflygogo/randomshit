# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o926. 積木城堡 (Castle)
# 2024-11 TOI 練習賽 潛力組


n = int(input())
data = [tuple(map(int, input().split()))[1:] for i in range(n)]
for i in range(n):
    data[i] = (max(data[i]), len(data[i]))
max_value = max(data)[0]
print(sum((max_value - i) * j for i, j in data if i < max_value))
