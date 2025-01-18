# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 905. Sort Array By Parity


from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums
