# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 977. Squares of a Sorted Array


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lft, rgt = 0, len(nums) - 1
        result = []
        while lft <= rgt:
            if abs(nums[lft]) > abs(nums[rgt]):
                result.append(nums[lft] ** 2)
                lft += 1
            else:
                result.append(nums[rgt] ** 2)
                rgt -= 1
        return result[::-1]


if __name__ == "__main__":
    test = [[-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11]]
    s = Solution()
    for i in test:
        print(s.sortedSquares(i))
