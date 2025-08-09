# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge 104. Maximum Depth of Binary Tree

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ bfs

    complexity:
        time: O(n)
        space: O(n)
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, cnt = queue.popleft()
            if cnt > result:
                result = cnt
            if node.left:
                queue.append((node.left, cnt + 1))
            if node.right:
                queue.append((node.right, cnt + 1))
        return result
