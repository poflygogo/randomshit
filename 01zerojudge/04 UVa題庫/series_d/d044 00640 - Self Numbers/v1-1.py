# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00640 Self Numbers
# ZeroJudge d044


TARGET = 1000000
nums = [True] * (TARGET + 1)

for i in range(1, TARGET + 1):
    if not nums[i]:
        continue
    
    i += sum(map(int, str(i)))
    while i <= TARGET:
        if not nums[i]:
            break
        nums[i] = False
        i += sum(map(int, str(i)))

print('\n'.join(map(str, filter(lambda x: nums[x], range(1, TARGET + 1)))))
