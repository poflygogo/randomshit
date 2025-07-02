# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f676. FJCU_109_Winter_Day2_Lab5 堆


class MaxHeap:
    """最大堆

    本質上就是二元樹，但用 list 模擬是實務上效率較高的作法，確實可以用下面這種形式實作:

    class Node:
        def __init__(self, val, lft=None, rgt=None, parent=None):
            self.val: int = val,
            self.lft: Node|None = lft,
            self.rgt: Node|None = rgt,
            self.parent: Node|None = parent

    但這種形式的缺點是插找節點的效率是 O(N), 相較於 list 的 O(1) 作法明顯慢一些。
    """

    def __init__(self):
        self.heap = []

    def insert(self, val: int):
        """插入元素"""
        self.heap.append(val)
        self._heapify_up()

    def pop(self):
        """從heap頂端取出元素(最大值)"""
        self._swap(0, len(self.heap) - 1)
        target = self.heap.pop()
        self._heapify_down()
        return target

    def _parent(self, idx: int):
        return (idx - 1) // 2

    def _child_lft(self, idx: int):
        return 2 * idx + 1

    def _child_rgt(self, idx: int):
        return 2 * idx + 2

    def _has_parent(self, idx: int):
        return self._parent(idx) >= 0

    def _has_child_lft(self, idx: int):
        return self._child_lft(idx) < len(self.heap)

    def _has_child_rgt(self, idx: int):
        return self._child_rgt(idx) < len(self.heap)

    def _swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _heapify_up(self):
        curr_idx = len(self.heap) - 1
        while (
            self._has_parent(curr_idx)
            and self.heap[self._parent(curr_idx)] < self.heap[curr_idx]
        ):
            self._swap(self._parent(curr_idx), curr_idx)
            curr_idx = self._parent(curr_idx)

    def _heapify_down(self):
        curr_idx = 0
        while self._has_child_lft(curr_idx):
            next_idx = self._child_lft(curr_idx)
            if (
                self._has_child_rgt(curr_idx)
                and self.heap[self._child_rgt(curr_idx)] > self.heap[next_idx]
            ):
                next_idx = self._child_rgt(curr_idx)
            if self.heap[curr_idx] >= self.heap[next_idx]:
                break
            self._swap(curr_idx, next_idx)
            curr_idx = next_idx


heap = MaxHeap()
while True:
    try:
        ipt = input().split()
        if ipt[0] == "I":
            heap.insert(int(ipt[1]))
        elif ipt[0] == "D":
            print(heap.pop())
    except EOFError:
        break
