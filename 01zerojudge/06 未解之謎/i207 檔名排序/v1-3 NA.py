# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge i207. 檔名排序


# ---------------------------------------------------

import sys
import io
Q = """2
f 1234 g 1333
f 12"""
sys.stdin = io.StringIO(Q.strip())

# ---------------------------------------------------



import re

def my_natsort_rule(s):
    temp = re.findall(r'\d+|\D+', s)
    for i in range(len(temp)):
        if temp[i].isdigit():
            temp[i] = (int(temp[i]), temp[i])
        else:
            temp[i] = (float('inf'), temp[i].upper() + '  ' * (temp[i][-1] != ' '))
    return tuple(temp)
        

data = [input() for _ in range(int(input()))]
data.sort(key=my_natsort_rule)
print('\n'.join(data))
