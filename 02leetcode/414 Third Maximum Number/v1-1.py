# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 414. Third Maximum Number


from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_values = set()
        for n in nums:
            if n in max_values:
                continue
            max_values.add(n)
            if len(max_values) > 3:
                max_values.remove(min(max_values))
        if len(max_values) < 3:
            return max(max_values)
        return min(max_values)
