# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 594. Longest Harmonious Subsequence


from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        data = Counter(nums)
        result = 0
        for i in data:
            if i + 1 in data:
                result = max(result, data[i] + data[i + 1])
        return result


if __name__ == "__main__":
    test = [[1, 3, 2, 2, 5, 2, 3, 7], [1, 2, 3, 4], [1, 1, 1, 1], [1, 2, 4, 4, 4]]

    s = Solution()
    for i in test:
        print(s.findLHS(i))
