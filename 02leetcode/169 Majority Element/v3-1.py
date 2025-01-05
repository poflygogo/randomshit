# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 169. Majority Element

# time : O(n)
# space: O(1)


from typing import List, Any


class Solution:
    def majorityElement(self, nums: List[int], count: int=0, candidate: Any=None) -> int:
        # Moore Voting Algorithm
        for i in nums:
            if count == 0:
                candidate = i
                count = 1
            elif candidate == i:
                count += 1
            else:
                count -= 1
        return candidate
