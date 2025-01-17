# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 53. Maximum Subarray

# Kadane's Algorithm to Maximum Sum Subarray Problem | Youtube
# https://www.youtube.com/watch?v=86CQq3pKSUw&t=666s


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # dp
        max_curr = max_global = nums[0]
        for i in range(1, len(nums)):
            max_curr = max(nums[i], max_curr + nums[i])
            if max_curr > max_global:
                max_global = max_curr
        return max_global


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-1]))
