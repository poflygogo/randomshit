# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o926. 積木城堡 (Castle)
# 2024-11 TOI 練習賽 潛力組


n = int(input())
arr = []
for _ in range(n):
    i, *nums = map(int, input().split())
    arr.append((max(nums), i))
max_value = max(arr)[0]
print(sum((max_value - i) * j for i, j in arr if i < max_value))
