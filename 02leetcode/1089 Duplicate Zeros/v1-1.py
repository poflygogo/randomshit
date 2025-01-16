# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1089. Duplicate Zeros


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1

