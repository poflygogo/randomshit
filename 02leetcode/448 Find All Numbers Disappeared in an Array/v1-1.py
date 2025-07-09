# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 448. Find All Numbers Disappeared in an Array


from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = set(nums)
        b = set(range(1, len(nums) + 1))
        return sorted(b.difference(a))
