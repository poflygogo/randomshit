# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00484 The Department of Redundancy Department
# ZeroJudge e618


nums = []
counter = []
for i in input().split():
    try:
        idx = nums.index(i)
    except ValueError:
        nums.append(i)
        counter.append(1)
    else:
        counter[idx] += 1

print('\n'.join(f'{nums[i]} {counter[i]}' for i in range(len(nums))))
