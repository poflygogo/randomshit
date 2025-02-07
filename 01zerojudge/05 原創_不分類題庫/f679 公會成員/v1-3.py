# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f679. 公會成員


from bisect import bisect_left as bisect


n, q = map(int, input().split())
nums = input().split()

# 只好用 in-place 的方式把資料轉換成 int 了
for i in range(n):
    nums[i] = int(nums[i])

for _ in range(q):
    target = int(input())
    idx = bisect(
        a=nums,
        x=target,
        hi=n
    )
    print('Yes' if nums[idx] == target else 'No')
