"""
AC(0.1s, 15.8MB)
O(n)
https://zerojudge.tw/ShowThread?postid=30963&reply=0
"""

from itertools import accumulate


input()
data = [int(i) for i in input().split()]
max_data = accumulate(data, max)
print(max(lft - rgt for lft, rgt in zip(max_data, data[1:])))
