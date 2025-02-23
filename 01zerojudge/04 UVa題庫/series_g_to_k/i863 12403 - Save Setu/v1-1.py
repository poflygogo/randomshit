# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12403 Save Setu
# ZeroJudge i863


total = 0
for _ in range(int(input())):
    info = input().split()
    if info[0] == 'donate':
        total += int(info[1])
    else:
        print(total)
