# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 169. Majority Element

# time : O(n)
# space: O(n)


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums) // 2
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] > major:
                return i
