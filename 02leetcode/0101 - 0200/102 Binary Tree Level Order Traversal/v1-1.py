# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 102. Binary Tree Level Order Traversal

from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = collections.deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if len(result) <= level:
                result.append([])
            result[level].append(node.val)
            queue.extend([(node.left, level + 1), (node.right, level + 1)])
        return result
