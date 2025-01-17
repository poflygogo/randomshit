# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 88. Merge Sorted Array


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()


if __name__ == '__main__':
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    s = Solution()
    s.merge(num1, 3, num2, 3)
    print(num1)
