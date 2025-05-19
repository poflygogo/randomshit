# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i207. 檔名排序


import re

def my_natsort_rule(s):
    temp = re.findall(r'\d+|\D+', s)
    for i in range(len(temp)):
        if temp[i].isdigit():
            temp[i] = (int(temp[i]), temp[i])
        else:
            temp[i] = (float('inf'), temp[i].upper())
    return tuple(temp)
        

data = [input() for _ in range(int(input()))]
data.sort(key=my_natsort_rule)
print('\n'.join(data))
