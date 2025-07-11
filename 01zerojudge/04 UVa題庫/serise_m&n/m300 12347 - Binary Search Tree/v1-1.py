# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12347 Binary Search Tree
# ZeroJudge m300


from typing import Optional
from sys import stdin


class Node:
    def __init__(self, val: int):
        self.val = val  # int
        self.lft = None # type: Optional[Node]
        self.rgt = None # type: Optional[Node]

class BinarySearchTree:
    def __init__(self):
        self.root = None # type: Optional[Node]
    
    def push(self, val: int):
        if self.root is None:
            self.root = Node(val)
        else:
            self._push(val, self.root)

    def _push(self, val: int, root: Node):
        if val < root.val:
            if root.lft:
                self._push(val, root.lft)
            else:
                root.lft = Node(val)
        else:
            if root.rgt:
                self._push(val, root.rgt)
            else:
                root.rgt = Node(val)
    
    def post_traversal(self) -> list:
        result = []
        self._post_traversal(result, self.root)
        return result
    
    def _post_traversal(self, arr: list, root: Optional[Node]):
        if root:
            self._post_traversal(arr, root.lft)
            self._post_traversal(arr, root.rgt)
            arr.append(root.val)

def main():
    tree = BinarySearchTree()
    for i in stdin:
        tree.push(int(i))
    print('\n'.join(map(str, tree.post_traversal())))


main()
