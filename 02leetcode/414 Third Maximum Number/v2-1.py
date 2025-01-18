# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 414. Third Maximum Number


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        return sorted(nums)[-3]
