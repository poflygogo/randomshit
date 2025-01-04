# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 40. Combination Sum II


from typing import List, Dict


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.combinationSum2_helper(candidates, target, [], len(candidates))
        return self.ans

    def combinationSum2_helper(self, iterable: List[int], target: int, comb: List[int], length: int, start_idx: int=0, temp_sum: int=0):
        if temp_sum == target:
            result = [iterable[i] for i in comb]
            if result not in self.ans:
                self.ans.append(result)
            return
        if temp_sum > target:
            return 
        for i in range(start_idx, length):
            comb.append(i)
            self.combinationSum2_helper(iterable, target, comb, length, i + 1, temp_sum + iterable[i])
            comb.pop()


if __name__ == '__main__':
    s = Solution()
    a = s.combinationSum2([1, 2, 3], 4)
    print(a)
