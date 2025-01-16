# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1295. Find Numbers with Even Number of Digits


from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                cnt += 1
        return cnt
