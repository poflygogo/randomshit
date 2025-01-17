# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 53. Maximum Subarray

# 前綴和，通過更多測資了，但還是 TLE


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        return max(prefix_sum[j] - prefix_sum[i] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-1]))
