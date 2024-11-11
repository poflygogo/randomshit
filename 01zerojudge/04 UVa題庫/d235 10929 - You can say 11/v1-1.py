# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10929 You can say 11
# ZeroJudge d235

while True:
    num = input().rstrip()
    if num == '0':
        exit()

    if (sum(int(num[i]) for i in range(0, len(num), 2)) - 
        sum(int(num[i]) for i in range(1, len(num), 2))) % 11 == 0:
        print(f'{num} is a multiple of 11.')
    
    else:
        print(f'{num} is not a multiple of 11.')
