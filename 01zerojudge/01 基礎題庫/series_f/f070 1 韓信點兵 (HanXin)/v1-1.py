# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f070. 1. 韓信點兵 (HanXin)
# TOI 2020-05 練習賽 新手組


data = dict(map(int, input().split()) for _ in range(3))
key = sorted(data)

i = 0
while True:
    num = key[2] * i + data[key[2]]
    if num % key[0] == data[key[0]] and num % key[1] == data[key[1]]:
        print(num)
        exit()
    
    i += 1
