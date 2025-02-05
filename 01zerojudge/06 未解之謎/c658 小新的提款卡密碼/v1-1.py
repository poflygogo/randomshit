# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c658. 小新的提款卡密碼

nums: dict[tuple, list]
i: int

from sys import stdin


nums = {}
for i in range(32, int(1e5)):   # 32 = math.ceil(math.sqrt(1000))
    i **= 2
    key = tuple(sorted(str(i)))
    if '0' in key:
        continue
    if key in nums:
        nums[key].append(i)
    else:
        nums[key] = [i]

for line in stdin:
    print(*nums.get(tuple(sorted(line.rstrip())), [0]))
