# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1299. Replace Elements with Greatest Element on Right Side

# TLE Solution
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i < len(arr) - 1:
                arr[i] = max(arr[j] for j in range(i + 1, len(arr)))
            else:
                arr[i] = -1
        return arr
