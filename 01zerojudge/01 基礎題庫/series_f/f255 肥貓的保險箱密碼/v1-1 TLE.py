# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f255. 肥貓的保險箱密碼


while True:
    num = int(input())
    if not num:
        break
    print(pow(2, num))
