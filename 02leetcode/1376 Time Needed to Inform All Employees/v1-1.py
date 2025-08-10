# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1376. Time Needed to Inform All Employees

from typing import List


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        times = [0] * n
        for i in range(n):
            j = i
            while manager[j] != -1:
                j = manager[j]
                times[i] += informTime[j]
        return max(times)


if __name__ == "__main__":
    s = Solution()
    print(s.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1]))
