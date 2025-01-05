# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 136. Single Number

# time : O(n)
# space: O(n)


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
