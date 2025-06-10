# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e880. Q1 合影隊形
# 100學年度台北高中電腦程式設計競賽 


# ---------------------------------------------------

import sys
import io
Q = """
4 
4 
A B 
C D 
C A 
C B
"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



from sys import stdin
from string import ascii_uppercase
from itertools import permutations
from collections import defaultdict


n, _, *info = stdin.read().split()
n = int(n)

info_dict = defaultdict(set)
for i in range(0, len(info), 2):
    info_dict[info[i]].add(info[i + 1])
    info_dict[info[i + 1]].add(info[i])

result = "No Solution"
for group in permutations(ascii_uppercase[:n], n):
    if not any(info_dict[group[i]].intersection({group[i - 1], group[i + 1]}) for i in range(1, n - 1)):
        result = ''.join(group)
        break

print(result)
