# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 977. Squares of a Sorted Array


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] **= 2
        nums.sort()
        return nums
