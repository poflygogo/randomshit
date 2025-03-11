# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge b573. 排列組合、最大公因數


from itertools import permutations
from math import gcd

for _ in range(int(input())):
    item, a, b = input().split()
    a, b = int(a) - 1, int(b) - 1
    nums = list(map(lambda x: int(''.join(x)), permutations(item, len(item))))
    nums.sort()
    print(gcd(nums[a], nums[b]))
