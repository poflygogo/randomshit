# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 100. Same Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q)

    def traversal(self, node: Optional[TreeNode]):
        # inorder
        result = []
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result
