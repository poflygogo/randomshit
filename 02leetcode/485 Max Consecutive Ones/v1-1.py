# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 485. Max Consecutive Ones


from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = maxCount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                maxCount = max(count, maxCount)
                count = 0
        return max(count, maxCount)
