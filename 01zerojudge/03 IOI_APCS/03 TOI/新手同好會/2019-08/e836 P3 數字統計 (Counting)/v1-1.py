# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e836 p3.數字統計 (Counting)
# 2019-08 TOI 新手同好會


n = int(input())
nums = list(map(int, input().split()))

counter = {}
for i in nums:
    counter[i] = counter.get(i, 0) + 1

print(len(counter))
counter_max = max(counter.values())
if len(counter) == len(nums):
    print('NO')
else:
    print(*[i for i, j in counter.items() if j == counter_max])
