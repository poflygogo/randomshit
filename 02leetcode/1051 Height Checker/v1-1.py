# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1051. Height Checker


from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                cnt += 1
        return cnt
