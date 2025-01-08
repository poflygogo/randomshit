# -*- encoding: utf-8 -*-
# python 3.12


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class SingleLinkList:
    def __init__(self, node=None):
        self._head = node
        
    def is_empty(self):
        """check if link list is empty"""
        return self._head is None

    def length(self):
        """return the number of items in the link list"""
        pass

    def travel(self):
        """return all items in the link list"""

    def add(self):
        """在鏈表頭部添加元素"""
        pass

    def append(self):
        """在末端添加元素"""
        pass
