# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f679. 公會成員


from bisect import bisect_left as bisect
from array import array


n, q = map(int, input().split())
nums = array('l', map(int, input().split()))

for _ in range(q):
    target = int(input())
    idx = bisect(
        a=nums,
        x=target,
        hi=n
    )
    print('Yes' if nums[idx] == target else 'No')
