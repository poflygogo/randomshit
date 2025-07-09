# -*- encoding: utf-8 -*-
# python 3.12
# LeetCode 328. Odd Even Linked List

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 把原本的 LinkList 拆分成兩組，分別跑奇數位和偶數位
    # 最後將偶數 LinkList 的頭連接到奇數 LinkList 的尾
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        odd = odd_head = head
        head = head.next

        if head is None:
            return odd_head
        even = even_head = head
        head = head.next

        cnt = 3
        while head is not None:
            if cnt % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            cnt += 1
        
        odd.next = even_head
        even.next = None
        return odd_head
