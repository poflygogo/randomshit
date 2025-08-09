# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 107. Binary Tree Level Order Traversal II

from typing import List, Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """ bfs + reverse

    執行一次 bfs 後，對結果 reverse 就是題目所要求的。
    也可以使用切片 result[::-1]，但會使用更多的空間，我個人不太建議。
    (這個語法實質上會創建一個新的陣列，而不是反轉原始陣列)
    """
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(temp)
        result.reverse()
        return result
