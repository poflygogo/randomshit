# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f675. FJCU_109_Winter_Day2_Lab3 二元搜尋樹

# ---------------------------------------------------

import sys
import io
Q = """
7
17
2
5
12
8
15
13
17
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


class Node:
    def __init__(self, val: int):
        self.val = val  # type: int
        self.lft = None # type: Node|None
        self.rgt = None # type: Node|None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val: int):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(val, self.root)

    def _insert(self, val: int, curr: Node):
        if curr.val > val:
            if curr.lft is None:
                curr.lft = Node(val)
            else:
                self._insert(val, curr.lft)
        else:
            if curr.rgt is None:
                curr.rgt = Node(val)
            else:
                self._insert(val, curr.rgt)
    
    def traversal_infix(self):
        def func(node: Node):
            if node.lft is not None:
                func(node.lft)
            result.append(node.val)
            if node.rgt is not None:
                func(node.rgt)

        result = []
        func(self.root)
        return result


if __name__ == '__main__':
    tree = BinarySearchTree()
    for _ in range(int(input())):
        tree.insert(int(input()))
    
    result = tree.traversal_infix()
    print(*result, sep='\n')
    print('Yes' if int(input()) in result else 'No')
