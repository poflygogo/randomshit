# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c299. 1. 連號或不連號


n, *nums = map(int, input().split())
nums.sort()
flag = nums[-1] - nums[0] == n - 1
print(nums[0], nums[-1], ('no', 'yes')[flag])
