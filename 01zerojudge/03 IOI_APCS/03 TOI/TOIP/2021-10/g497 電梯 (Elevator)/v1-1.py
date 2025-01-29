# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g497. 電梯 (Elevator)
# 2021-10 TOI 練習賽 新手組


n = int(input())
arr = [1] + list(map(int, input().split()))
result = 0
for i in range(1, n + 1):
    result += (arr[i] - arr[i - 1]) * (3 if arr[i] >= arr[i - 1] else -2)
print(result)
