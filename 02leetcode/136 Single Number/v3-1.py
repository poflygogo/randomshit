# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 136. Single Number

# time : O(n)
# space: O(1)


from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result
