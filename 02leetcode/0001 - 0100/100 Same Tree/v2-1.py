# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 100. Same Tree

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversal(p) == self.traversal(q)

    def traversal(self, node: Optional[TreeNode]):
        # lever-order, bfs, included None nodes.
        if node is None:
            return []
        result = [node.val]
        queue = collections.deque([node])
        while queue:
            curr = queue.popleft()
            
            if curr:
                result.append(curr.val)
                queue.extend([curr.left, curr.right])
            else:
                result.append(None)
        return result
