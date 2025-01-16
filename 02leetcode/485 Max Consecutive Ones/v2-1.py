# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 485. Max Consecutive Ones


from typing import List
import itertools


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        for i, j in itertools.groupby(nums):
            if i == 1:
                result = max(result, len(list(j)))
        return result
