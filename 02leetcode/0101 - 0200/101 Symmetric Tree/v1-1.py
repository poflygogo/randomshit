# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 101. Symmetric Tree

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ BFS, Level-Order
    
    把根節點底下的兩個節點視為兩個子樹的樹根，比較這兩個子樹是否對稱

    complexity:
        time: O(N)
        space: O(N)
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        queue = collections.deque([(root.left, root.right)])
        while queue:
            lft, rgt = queue.popleft()
            if (lft is None) != (rgt is None):
                return False
            if lft:
                if lft.val != rgt.val:
                    return False
                queue.append((lft.left, rgt.right))
                queue.append((lft.right, rgt.left))
        return True
