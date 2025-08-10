# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 111. Minimum Depth of Binary Tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result = float("inf")

        def _impl(curr: TreeNode, depth: int = 1):
            if curr.left is None and curr.right is None:
                nonlocal result
                if result > depth:
                    result = depth
                return
            if curr.left:
                _impl(curr.left, depth + 1)
            if curr.right:
                _impl(curr.right, depth + 1)

        if root:
            _impl(root)
            return result
        else:
            return 0
