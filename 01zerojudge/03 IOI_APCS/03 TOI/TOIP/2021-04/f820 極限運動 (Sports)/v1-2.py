# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f820. 極限運動 (Sports)
# 2021-04 TOI 練習賽 新手組


n = int(input())
data = tuple(map(int, input().split()))
idx = int(input()) - 1

offset = 1 if idx == 0 or idx < n - 2 and data[idx + 1] < data[idx - 1] else -1
while 0 <= idx < n and data[idx + offset] <= data[idx]:
    idx += offset

print(idx + 1)
