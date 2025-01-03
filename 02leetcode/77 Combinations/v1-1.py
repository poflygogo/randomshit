# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 77. Combinations

# C(n, k)


from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.combine_helper(n, k)
        return self.result

    def combine_helper(self, n, k, comb=None, start=1):
        if comb is None:
            comb = []
        if len(comb) == k:
            self.result.append(comb.copy())
            return
        if len(comb) + (n - start) + 1< k:
            return
        for i in range(start, n + 1):
            comb.append(i)
            self.combine_helper(n, k, comb, i + 1)
            comb.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.combine(3, 2))
