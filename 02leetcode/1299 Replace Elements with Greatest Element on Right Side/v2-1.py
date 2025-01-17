# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1299. Replace Elements with Greatest Element on Right Side


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_idx = 0
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            elif i != max_idx:
                arr[i] = arr[max_idx]
            else:
                max_idx += 1
                for j in range(i + 2, len(arr)):
                    if arr[j] > arr[max_idx]:
                        max_idx = j
                arr[i] = arr[max_idx]
        return arr
