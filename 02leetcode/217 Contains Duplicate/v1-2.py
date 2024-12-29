# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 217. Contains Duplicate


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for i in nums:
            if i in temp:
                return True
            temp.add(i)
        return False
