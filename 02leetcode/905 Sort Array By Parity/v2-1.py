# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 905. Sort Array By Parity


from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lft, rgt = 0, len(nums) - 1
        while lft < rgt:
            while lft < rgt and nums[lft] % 2 == 0:
                lft += 1
            while lft < rgt and nums[rgt] % 2 != 0:
                rgt -= 1
            nums[lft], nums[rgt] = nums[rgt], nums[lft]
        return nums
