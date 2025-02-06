# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c531. 基礎排序 #1-1 ( 偶數排序 )


from sys import stdin


for line in stdin:
    line = list(map(int, line.rstrip().split(',')))
    even = [i for i in line if i & 1 == 0]
    even.sort()
    j = 0
    for i in range(len(line)):
        if line[i] & 1 == 0:
            line[i] = even[j]
            j += 1
    print(','.join(map(str, line)))
