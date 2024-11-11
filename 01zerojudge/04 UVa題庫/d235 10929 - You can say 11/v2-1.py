# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10929 You can say 11
# ZeroJudge d235

while True:
    num = input().rstrip()
    if num == '0':
        exit()

    print(f'{num} is {"not " if int(num) % 11 else ""}a multiple of 11.')
