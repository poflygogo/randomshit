# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q255. 剪刀石頭布 - 數手指


n = int(input())
for t in range(1, n + 1):
    a, b = map(int, input().split())
    
    for paper in range(a // 5, -1, -1):
        scissor = (b - 5*paper) // 2
        rock = a - scissor - paper
        if rock >= 0:
            break
    else:
        rock = 'Invalid'

    print(f'Game {t:02d}: {rock}')
