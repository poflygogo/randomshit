# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 169. Majority Element

# time : O(n)
# space: O(n)


from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common(1)
