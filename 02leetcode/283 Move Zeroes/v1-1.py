# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 283. Move Zeroes


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        nums[j:] = [0] * (len(nums) - j)
