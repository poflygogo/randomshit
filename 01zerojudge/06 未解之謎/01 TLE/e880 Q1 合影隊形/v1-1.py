# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e880. Q1 合影隊形
# 100學年度台北高中電腦程式設計競賽 


from string import ascii_uppercase
from itertools import permutations

n = int(input())
info = {}
for _ in range(int(input())):
    a, b = input().rstrip().split()
    info[a] = info.get(a, set()).union({b})
    info[b] = info.get(b, set()).union({a})

result = "No Solution"
for group in permutations(ascii_uppercase[:n], n):
    if all(info.get(group[i], set()).intersection({group[i - 1], group[i + 1]}) == set() for i in range(1, n - 1)):
        result = ''.join(group)
        break

print(result)
