# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 39. Combination Sum


from typing import List


class Solution:
    def __init__(self):
        self.result = []
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinationSum_helper(candidates, target, len(candidates), [])
        return sorted(self.result)
    
    def combinationSum_helper(
            self,
            iterable: List[int],
            target: int,
            length: int,
            comb: List[int],
            start_idx: int=0,
            temp_sum: int=0):
        if temp_sum == target:
            self.result.append([iterable[i] for i in comb])
            return
        if temp_sum > target:
            return
        for i in range(start_idx, length):
            comb.append(i)
            self.combinationSum_helper(iterable, target, length, comb, i, temp_sum + iterable[i])
            comb.pop()
