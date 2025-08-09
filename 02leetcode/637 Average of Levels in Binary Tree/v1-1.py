# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 637. Average of Levels in Binary Tree

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if root is None:
            return result
        queue = [root]
        while queue:
            temp = []
            result.append(round(sum(i.val for i in queue) / len(queue), 5))
            for i in queue:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
        return result
