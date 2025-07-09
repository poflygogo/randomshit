# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 2. Add Two Numbers


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 建立一個假的頭節點，本身沒有任何意義，僅輔助創建後續節點
        # 最後直接輸出 dummy_head.next 就是答案了
        dummy_head = curr = ListNode(0)
        temp = 0

        # 滿足條件才新增節點(進位)
        while l1 or l2 or temp:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            temp += a + b

            temp, reminder = divmod(temp, 10)
            curr.next = ListNode(reminder)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
