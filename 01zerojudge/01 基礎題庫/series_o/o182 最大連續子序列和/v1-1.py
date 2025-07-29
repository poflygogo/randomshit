# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o182. 最大連續子序列和


n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i, n):
        t = sum(nums[i:j])
        if result < t <= k:
            result = t

print(result)
