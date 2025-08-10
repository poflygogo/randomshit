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
        if root is None:
            return 0
        
        depth = 1
        curr_level = [root]
        while curr_level:
            next_level = []
            for node in curr_level:
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            depth += 1
            curr_level = next_level
            
        return depth
