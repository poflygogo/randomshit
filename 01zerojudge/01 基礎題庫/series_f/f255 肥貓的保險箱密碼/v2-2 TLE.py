# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f255. 肥貓的保險箱密碼


from sys import stdin


seen = {}
nums = stdin.read().splitlines()
for i in nums:
    i = i.strip()
    if i == '0':
        break
    result = seen.setdefault(i, 2 ** int(i))
    print(result)
