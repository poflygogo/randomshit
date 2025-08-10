# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 429. N-ary Tree Level Order Traversal

from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(
        self, val: Optional[int] = None, children: Optional[List["Node"]] = None
    ):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if root is None:
            return []
        result = []
        level_curr = [root]
        while level_curr:
            level_next = []
            vals = []
            for i in level_curr:
                vals.append(i.val)
                if i.children:
                    level_next.extend(i.children)
            level_curr = level_next
            result.append(vals)
        return result
