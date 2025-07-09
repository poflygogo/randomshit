# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 448. Find All Numbers Disappeared in an Array


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
