# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 47. Permutations II

from typing import List
import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        elements = collections.Counter(nums)
        length = len(nums)
        return [i for i in self._impl(elements, length, [])]

    def _impl(self, elements: collections.Counter, length: int, path: List[int]):
        if len(path) == length:
            yield path.copy()
            return
        
        for i in elements:
            if elements[i] > 0:
                elements[i] -= 1
                path.append(i)
                yield from self._impl(elements, length, path)
                elements[i] += 1
                path.pop()
