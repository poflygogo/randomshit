# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 3201. Find the Maximum Length of Valid Subsequence I


from typing import List


class Solution:
    """
    有四種狀態，四種都一起 dp
      - 全部都偶數
      - 全部都奇數
      - 奇偶交錯，由奇數開始
      - 奇偶交錯，由偶數開始
    """
    def maximumLength(self, nums: List[int]) -> int:
        all_odd = switch_start_odd = int(nums[0] % 2 != 0)
        all_even = switch_start_even = int(nums[0] % 2 == 0)
        switch_start_odd_pre = switch_start_even_pre = bool(switch_start_odd)
        for i in range(1, len(nums)):
            is_odd = nums[i] % 2 != 0
            if is_odd:
                all_odd += 1
            else:
                all_even += 1
            
            if (switch_start_odd_pre and not is_odd) or (not switch_start_odd_pre and is_odd):
                switch_start_odd += 1
                switch_start_odd_pre ^= True

            if (switch_start_even_pre and not is_odd) or (not switch_start_even_pre and is_odd):
                switch_start_even += 1
                switch_start_even_pre ^= True

        return max(all_even, all_odd, switch_start_even, switch_start_odd)


if __name__ == "__main__":
    test = [[1, 2, 3, 4], [1, 2, 1, 1, 2, 1, 2], [1, 3], [2, 3]]
    s = Solution()
    for i in test:
        print(s.maximumLength(i))
