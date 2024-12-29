# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 217. Contains Duplicate


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = dict()
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] > 1:
                return True
        return False
