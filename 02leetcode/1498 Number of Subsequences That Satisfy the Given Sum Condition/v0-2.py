# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition


from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = int(1e9) + 7
        nums.sort()

        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = (powers[i - 1] * 2) % MOD

        cnt = 0
        for lft in range(len(nums)):
            if nums[lft] * 2 > target:
                break
            for rgt in range(len(nums) - 1, lft - 1, -1):
                if nums[lft] + nums[rgt] <= target:
                    cnt = (cnt + powers[rgt - lft]) % MOD
                    break
        return cnt


if __name__ == "__main__":
    test = [([3, 5, 6, 7], 9), ([3, 3, 6, 8], 10), ([2, 3, 3, 4, 6, 7], 12)]
    s = Solution()
    for nums, target in test:
        print(s.numSubseq(nums, target))


# [1, 2, 3, 4], 5

# [1]
# [1, 2], [1, 3], [1, 4]
# [1, 2, 3], [1, 2, 4], [1, 3, 4]
# [1, 2, 3, 4]
