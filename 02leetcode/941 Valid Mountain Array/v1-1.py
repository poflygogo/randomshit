# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 941. Valid Mountain Array


from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        increasing = True
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                return False
            elif increasing and arr[i] < arr[i - 1]:
                if i == 1:
                    return False
                increasing = False
            elif not increasing and arr[i] > arr[i - 1]:
                return False
        if not increasing:
            return True
        return False
