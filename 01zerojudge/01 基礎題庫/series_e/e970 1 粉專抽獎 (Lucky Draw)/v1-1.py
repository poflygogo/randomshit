# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e970. 1. 粉專抽獎 (Lucky Draw)
# 2019-04 TOI 練習賽 新手組


n = int(input())
nums = tuple(map(int, input().split()))
idx = sum(nums[i] for i in range(0, n, nums[-1])) % n
print(idx if idx else n, nums[idx - 1])
