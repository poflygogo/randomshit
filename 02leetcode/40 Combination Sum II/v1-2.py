# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 40. Combination Sum II


from typing import List, Dict


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.combinationSum2_helper(candidates, target, [])
        return self.ans

    def combinationSum2_helper(self, iterable: List[int], target: int, comb: List[int], start_idx: int=0):
        if target < 0:
            return
        if target == 0:
            self.ans.append(comb.copy())
            return
        for i in range(start_idx, len(iterable)):
            if i > start_idx and iterable[i] == iterable[i - 1]:
                continue
            self.combinationSum2_helper(
                iterable=iterable,
                target=target - iterable[i],
                comb=comb + [iterable[i]],
                start_idx=i + 1
            )


if __name__ == '__main__':
    s = Solution()
    a = s.combinationSum2([1, 2, 3], 4)
    print(a)
