# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


from itertools import permutations


input()
data = input().split()
data.sort(key=int)
for item in permutations(data):
    print(' '.join(item))
