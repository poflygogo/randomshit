# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1498. Number of Subsequences That Satisfy the Given Sum Condition


from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        cnt = 0
        for lft in range(len(nums)):
            if nums[lft] * 2 > target:
                break
            cnt += 1
            for rgt in range(lft + 1, len(nums)):
                if nums[lft] + nums[rgt] > target:
                    break
                cnt += 2 ** (rgt - lft - 1)
        return cnt % (int(1e9) + 7)


if __name__ == "__main__":
    test = [([3, 5, 6, 7], 9), ([3, 3, 6, 8], 10), ([2, 3, 3, 4, 6, 7], 12)]
    s = Solution()
    for nums, target in test:
        print(s.numSubseq(nums, target))
