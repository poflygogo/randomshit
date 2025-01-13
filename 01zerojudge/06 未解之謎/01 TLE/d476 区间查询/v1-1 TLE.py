# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d476. 区间查询


n, m = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(m):
    action, *args = input().split()
    args = list(map(int, args))
    if action == 'Q':
        print(sorted(nums[args[0] - 1:args[1]])[args[2] - 1])
    else:
        nums[args[0] - 1] = args[1]
