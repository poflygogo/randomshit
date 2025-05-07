# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a513. 最大值


import heapq

EMPTY_TEXT = "It's empty!"
for test_case in range(1, int(input()) + 1):
    print(f'Case {test_case}:')
    _, m = map(int, input().split())
    nums = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(nums)
    for _ in range(m):
        command = tuple(map(int, input().split()))
        if command[0] == 1:
            heapq.heappush(nums, -command[1])
        elif command[0] == 2 and nums:
            print(f'Max: {-heapq.heappop(nums)}')
        else:
            print(EMPTY_TEXT)
    nums.sort()
    if nums:
        print(' '.join(map(lambda x: str(-x), nums)))
    else:
        print(EMPTY_TEXT)
