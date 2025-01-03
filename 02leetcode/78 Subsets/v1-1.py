# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 78. Subsets


from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subset_helper(nums, [], len(nums))
        return self.ans

    def subset_helper(self, iterable: List[int], result: List[int], length, start_idx: int=0):
        self.ans.append(result.copy())
        for i in range(start_idx, length):
            result.append(iterable[i])
            self.subset_helper(iterable, result, length, i + 1)
            result.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
