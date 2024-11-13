# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12602 Nice Licence Plates
# ZeroJudge e505

for _ in range(int(input())):
    plate = input().rstrip().split('-')

    if abs(sum((ord(char) - 65) * 26 ** mul for char, mul in zip(plate[0], (2, 1, 0))) - int(plate[1])) <= 100:
        print('nice')
    
    else:
        print('not nice')
