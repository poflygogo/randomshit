# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 594. Longest Harmonious Subsequence


from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        data = Counter(nums)
        item = sorted(data)
        hs = [
            data[item[i]] + data[item[i + 1]]
            for i in range(len(item) - 1)
            if (item[i + 1] - item[i]) == 1
        ]
        return max(hs) if hs else 0


if __name__ == "__main__":
    test = [[1, 3, 2, 2, 5, 2, 3, 7], [1, 2, 3, 4], [1, 1, 1, 1], [1, 2, 4, 4, 4]]

    s = Solution()
    for i in test:
        print(s.findLHS(i))
