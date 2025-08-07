# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 101. Symmetric Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ DFS

    complexity:
        time: O(N)
        space: O(N)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root and self._is_mirror(root.left, root.right)
    
    def _is_mirror(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        return n1.val == n2.val and self._is_mirror(n1.left, n2.right) and self._is_mirror(n1.right, n2.left)
