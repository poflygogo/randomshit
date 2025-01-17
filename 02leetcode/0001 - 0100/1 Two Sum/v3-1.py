# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 1 Two Sum


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visit = {}
        for i in range(len(nums)):
            if nums[i] in visit:
                return [visit[nums[i]], i]
            visit[target - nums[i]] = i
