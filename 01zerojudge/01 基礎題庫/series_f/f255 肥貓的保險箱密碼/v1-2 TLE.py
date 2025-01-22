# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f255. 肥貓的保險箱密碼


seen = {}
while True:
    num = int(input())
    if not num:
        break
    result = seen.setdefault(num, pow(2, num))
    print(result)
