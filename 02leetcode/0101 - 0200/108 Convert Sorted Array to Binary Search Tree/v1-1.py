# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 108. Convert Sorted Array to Binary Search Tree

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._impl(nums, 0, len(nums))

    def _impl(self, nums: List[int], lft: int, rgt: int):
        if rgt == lft:
            return None
        mid = (lft + rgt) // 2
        node = TreeNode(nums[mid])
        node.left = self._impl(nums, lft, mid)
        node.right = self._impl(nums, mid + 1, rgt)
        return node


if __name__ == "__main__":
    s = Solution()
    res = s.sortedArrayToBST([-10, -3, 0, 5, 9])
