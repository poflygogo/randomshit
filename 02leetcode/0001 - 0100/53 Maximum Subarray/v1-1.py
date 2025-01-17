# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 53. Maximum Subarray

# 暴力解，穩吃 TLE


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-1]))
