# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 918. Maximum Sum Circular Subarray


from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_curr = min_curr = max_global = min_global = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            min_curr = min(nums[i], min_curr + nums[i])
            max_global = max(max_global, max_curr)
            min_global = min(min_global, min_curr)
        
        total = sum(nums)
        if min_global == total:
            return max_global
        else:
            return max(max_global, total - min_global)
