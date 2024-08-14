"""
math的ceil()可以用來處理數字的無條件進位
"""

from math import ceil

n, x = map(int, input().split())
print(ceil(n/x))
