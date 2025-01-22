# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f255. 肥貓的保險箱密碼


nums = [0] * 10000
nums[0] = 2
for i in range(1, 10000):
    nums[i] = nums[i - 1] << 1

while True:
    n = int(input())
    if not n:
        break
    print(nums[n - 1])
