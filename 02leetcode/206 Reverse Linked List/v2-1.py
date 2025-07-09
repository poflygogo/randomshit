# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 206. Reverse Linked List


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(
        self, head: Optional[ListNode], prev: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        # recursive
        if head is None:
            return prev
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
        return self.reverseList(head, prev)
