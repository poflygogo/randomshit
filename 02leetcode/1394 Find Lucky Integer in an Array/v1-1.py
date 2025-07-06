# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge 1394. Find Lucky Integer in an Array


from typing import List
import collections


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        for i, j in collections.Counter(arr).items():
            if i == j:
                lucky = max(lucky, i)
        return lucky
