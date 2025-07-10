# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d526. Binary Search Tree (BST)


from typing import Optional


class Node:
    def __init__(self, val: int):
        self.val = val  # type: int
        self.lft = None  # type: Optional[Node]
        self.rgt = None  # type: Optional[Node]


class BinarySearchTree:
    def __init__(self, args: list):
        self.root = Node(args[0])
        self._generate(args)

    def _generate(self, args: list):
        for i in range(1, len(args)):
            self._push(args[i], self.root)

    def _push(self, n: int, curr: Node):
        if n < curr.val:
            if curr.lft is None:
                curr.lft = Node(n)
            else:
                self._push(n, curr.lft)
        else:
            if curr.rgt is None:
                curr.rgt = Node(n)
            else:
                self._push(n, curr.rgt)

    def pre_traversal(self, arr: list, node: Optional[Node]):
        if node is not None:
            arr.append(node.val)
            self.pre_traversal(arr, node.lft)
            self.pre_traversal(arr, node.rgt)
    
    def __str__(self):
        arr = []
        self.pre_traversal(arr, self.root)
        return ' '.join(map(str, arr))


while True:
    try:
        input()
        nums = list(map(int, input().split()))
        s = BinarySearchTree(nums)
        print(s)
    except EOFError:
        break
