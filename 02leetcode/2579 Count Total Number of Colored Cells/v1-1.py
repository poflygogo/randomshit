# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 2579. Count Total Number of Colored Cells


class Solution:
    def coloredCells(self, n: int) -> int:
        return (n * 2 - 1) ** 2 - 4 * (n * (n-1) // 2)


if __name__ == '__main__':
    s = Solution()
    for i in range(1, 10):
        print(s.coloredCells(i))
