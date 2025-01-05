# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 169. Majority Element

# time : O(n log n)
# space: O(1)


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
