# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e942. pC. 數字排列
# 2009大學學測推甄申請二階


from itertools import permutations


input()
data = list(map(int, input().split()))
data.sort()
for item in permutations(data):
    print(*item)
