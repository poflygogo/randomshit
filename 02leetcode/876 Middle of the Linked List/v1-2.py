# encoding: utf-8
# Python 3.12
# LeetCode 876. Middle of the Linked List


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.append(head)
            head = head.next
        return temp[len(temp) // 2]
