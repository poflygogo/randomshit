# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge p908. 地底寶藏 (TreasureBox)
# TOI練習賽202504新手組第3題


n = int(input())
arr = list(map(int, input().split()))

x = float("inf")
x_idx = 0
flag = False
for i in range(n):
    if arr[i] < x:
        x = arr[i]
        x_idx = i
        flag = False
    elif arr[i] == x:
        x_idx = i
        flag = True

if not flag:
    y = arr[(x_idx + x) % n]
else:
    y = arr[(x_idx - x) % n]

print(arr[(y - 1) % n])
