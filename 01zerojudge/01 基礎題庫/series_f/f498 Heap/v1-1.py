# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f498. Heap


class Heap:
    def __init__(self, is_min_heap: bool= False):
        self.heap = []
        self.mode = is_min_heap

    def push(self, val: int):
        self.heap.append(val)
        self._heapify_up()

    def _parent(self, idx: int):
        return (idx - 1) // 2

    def _has_parent(self, idx: int):
        return self._parent(idx) >= 0
    
    def _swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _heapify_up(self):
        curr_idx = len(self.heap) - 1
        if self.mode:
            while (
                self._has_parent(curr_idx)
                and self.heap[self._parent(curr_idx)] < self.heap[curr_idx]
            ):
                self._swap(self._parent(curr_idx), curr_idx)
                curr_idx = self._parent(curr_idx)
        else:
            while (
                self._has_parent(curr_idx)
                and self.heap[self._parent(curr_idx)] > self.heap[curr_idx]
            ):
                self._swap(self._parent(curr_idx), curr_idx)
                curr_idx = self._parent(curr_idx)


def operate(arr: list, mode=False):
    result = Heap(mode)
    for i in arr:
        result.push(i)
    return result


while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))

        r1 = operate(arr, False)
        r2 = operate(arr, True)

        print(*r1.heap)
        print(*r2.heap)

    except EOFError:
        break
