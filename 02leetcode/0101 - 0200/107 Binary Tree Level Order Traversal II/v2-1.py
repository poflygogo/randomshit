# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 107. Binary Tree Level Order Traversal II

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ bfs + dfs

    透過 dfs 的性質，讓最底層的元素優先 append 到陣列中，最後才 append 樹根。
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def _impl(temp: List):
            if temp:
                curr = []
                next = []
                for i in temp:
                    curr.append(i.val)
                    if i.left:
                        next.append(i.left)
                    if i.right:
                        next.append(i.right)
                _impl(next)
                result.append(curr)

        if root is not None:
            _impl([root])
        return result
