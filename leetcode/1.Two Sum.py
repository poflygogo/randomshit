class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in nums:
            index_b = nums.index(a) + 1
            while index_b < len(nums):
                if a + nums[index_b] == target:
                    return [nums.index(a),index_b]
                index_b += 1
