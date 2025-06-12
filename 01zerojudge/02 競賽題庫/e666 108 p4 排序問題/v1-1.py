# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e666. 108 p4. 排序問題
# 108新北市資訊學科能力複賽


from collections import Counter
from string import ascii_uppercase
from itertools import accumulate
from bisect import bisect_left

n, m = map(int, input().split())
alpha = Counter(input().rstrip())
arr = list(accumulate([alpha[i] for i in ascii_uppercase]))
result = [ascii_uppercase[bisect_left(arr, i)] for i in map(int, input().split())]
print(''.join(result))
