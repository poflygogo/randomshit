# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f675. FJCU_109_Winter_Day2_Lab3 二元搜尋樹

# ---------------------------------------------------

import sys
import io
Q = """
7
17
2
5
12
8
15
13
17
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------


arr = [int(input()) for _ in range(int(input()))]
arr.sort()
print(*arr, sep='\n')
print('Yes' if int(input()) in arr else 'No')
