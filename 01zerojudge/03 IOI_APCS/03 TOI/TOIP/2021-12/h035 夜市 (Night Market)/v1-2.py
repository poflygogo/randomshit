# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h035. 夜市 (Night Market)
# 2021-12 TOI 練習賽 新手組


n = int(input())
action = map(int, input().split())

data = [[True, 0] for _ in range(9)]
score = 0

for i in action:
    for j in range(9):
        if data[j][1] > 0:
            data[j][1] -= 1
    
    if i != -1 and data[i - 1][0]:
        data[i - 1][0] = False
        data[i - 1][1] = 12
        score += i
    
    if all(j[1] != 0 for j in data):
        print('perfect')
        break
else:
    print(score)
