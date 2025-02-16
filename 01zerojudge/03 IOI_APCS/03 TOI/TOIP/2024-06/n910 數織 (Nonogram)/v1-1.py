# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge n910. 數織 (Nonogram)
# 2024-06 TOI 練習賽 新手組 第一題


n = int(input())
data = [input().split() for _ in range(n)]

for col in range(n):
    temp = [0]
    flag = True
    for row in range(n):
        if flag:
            if data[row][col] == '1':
                temp[-1] += 1
            elif temp[-1] != 0:
                flag = False
        elif data[row][col] == '1':
            if temp[-1] == 0:
                temp[-1] += 1
            else:
                temp.append(1)
            flag = True
    print(' '.join(map(str, temp)))

for row in data:
    temp = [0]
    flag = True
    for c in row:
        if flag:
            if c == '1':
                temp[-1] += 1
            elif temp[-1] != 0:
                flag = False
        elif c == '1':
            if temp[-1] == 0:
                temp[-1] += 1
            else:
                temp.append(1)
            flag = True
    print(' '.join(map(str, temp)))
