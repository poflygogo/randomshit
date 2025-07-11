# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 94. Binary Tree Inorder Traversal

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self._inorderTraversal(result, root)
        return result

    def _inorderTraversal(self, arr: List[int], node: TreeNode):
        if node is not None:
            self._inorderTraversal(arr, node.left)
            arr.append(node.val)
            self._inorderTraversal(arr, node.right)
