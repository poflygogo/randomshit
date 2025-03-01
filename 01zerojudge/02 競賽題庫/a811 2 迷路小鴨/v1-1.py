# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a811. 2. 迷路小鴨
# 102學年度高雄市資訊學科能力競賽複賽


from math import gcd
from functools import reduce

for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    diff = reduce(gcd, [arr[i] - arr[i - 1] for i in range(1, n)])
    print(diff)
