# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00122 Trees on the level
# ZeroJudge c101


from typing import Optional
from sys import stdin


class Node:
    def __init__(self, val: int):
        self.val = val  # type: int
        self.lft = None  # type: Optional[Node]
        self.rgt = None  # type: Optional[Node]


def main():
    ipt = stdin.read().split()
    arr = []
    for node_info in map(lambda x: x.strip("()").split(","), ipt):
        if len(node_info) > 1:
            arr.append(node_info)
        else:
            arr.sort(key=lambda x: (len(x[1]), x[1]))
            if is_tree(arr):
                print(" ".join(str(i[0]) for i in arr))
            else:
                print("not complete")
            arr.clear()


def is_tree(arr) -> bool:
    # 檢查是否有根節點
    if arr[0][1] != "":
        return False
    root = Node(int(arr[0][0]))
    for i in range(1, len(arr)):
        # 檢查是否有多餘的樹根
        if arr[i][1] == "":
            return False
        curr = root

        # 尋找父節點，找不到就直接返回 False
        for j in arr[i][1][:-1]:
            if j == "L":
                if curr.lft:
                    curr = curr.lft
                else:
                    return False
            elif j == "R":
                if curr.rgt:
                    curr = curr.rgt
                else:
                    return True

        # 插入新節點，如果欲插入的位置已經有其他節點就返回 False
        if arr[i][1][-1] == "L" and curr.lft is None:
            curr.lft = Node(int(arr[i][0]))
        elif arr[i][1][-1] == "R" and curr.rgt is None:
            curr.rgt = Node(int(arr[i][0]))
        else:
            return False
    return True


main()
