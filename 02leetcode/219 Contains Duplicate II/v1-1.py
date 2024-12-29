# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 219. Contains Duplicate II


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        temp = dict()
        for i, n in enumerate(nums):
            if n in temp and i - temp[n][-1] <= k:
                return True
            temp.setdefault(n, []).append(i)
        return False
