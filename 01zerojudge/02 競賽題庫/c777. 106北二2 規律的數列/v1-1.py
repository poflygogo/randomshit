# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c777. 106北二2.規律的數列
# 106北二區桃竹苗資訊學科能力複賽


from bisect import bisect_left

arr = [0, 1, 2, 3]
n, m = map(int, input().split())

while arr[-1] <= m:
    arr.append(arr[-1] * 2 - arr[-4])

idx = bisect_left(arr, n)
print(len(arr) - idx - 1)
