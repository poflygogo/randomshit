# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e284. 放暑假了!!!!!


from sys import stdin

nums = [0] * 33
nums[0] = 1
for i in range(1, 33):
    nums[i] = 2 * nums[i - 1]
nums = frozenset(nums)

for n in stdin:
    print('Yes' if int(n.rstrip()) in nums else 'No')
