# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1299. Replace Elements with Greatest Element on Right Side


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_value = max_value, max(max_value, arr[i])
        return arr
