# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 941. Valid Mountain Array


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        lft, rgt = 0, len(arr) - 1
        while lft < rgt and arr[lft] < arr[lft + 1]:
            lft += 1
        while rgt > 0 and arr[rgt] < arr[rgt - 1]:
            rgt -= 1
        return 0 < lft == rgt < len(arr) - 1
