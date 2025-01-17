# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 90. Subsets II


from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.backtrack(nums, [])
        return self.ans

    def backtrack(self, iterable: List[int], comb: List[int], start_idx: int=0):
        self.ans.append(comb.copy())
        for i in range(start_idx, len(iterable)):
            if i > start_idx and iterable[i] == iterable[i - 1]:
                continue
            self.backtrack(
                iterable,
                comb + [iterable[i]],
                i + 1
            )


if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2, 2]))
