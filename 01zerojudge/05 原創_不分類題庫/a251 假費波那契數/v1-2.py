# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge a251. 假費波那契數


def mainloop():
    for _ in range(int(input())):
        nums = list(map(int, input().split()))
        target = nums.pop(0)
        for _ in range(target - 4):
            nums.append(nums[-1] + nums[-4])
        nums.sort()
        print(nums[target // 2])


mainloop()
