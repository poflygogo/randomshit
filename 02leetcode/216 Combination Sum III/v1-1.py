# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 216. Combination Sum III


from typing import List


class Solution:
    def __init__(self):
        self.ans = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combinationSum3_helper(k, n, [])
        return self.ans

    def combinationSum3_helper(self, k: int, target: int, comb: List[int], start_idx: int=1, temp_sum: int=0):
        if temp_sum > target:
            return
        if len(comb) == k:
            if temp_sum == target:
                self.ans.append(comb.copy())
            return
        for i in range(start_idx, 10):
            comb.append(i)
            self.combinationSum3_helper(k, target, comb, i + 1, temp_sum + i)
            comb.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum3(3, 7))
