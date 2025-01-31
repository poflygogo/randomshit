# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j180. 戰備存糧 (Food)
# 2022-10 TOI 練習賽 新手組


barn_info = list(map(int, input().split()))

while barn_info[0] != -1:
    curr = total = barn_info[0] * barn_info[1]  # cost: 剩餘糧食 # total: 初始糧食
    cost = barn_info[0] # cost: 守衛數量
    day = 0
    while curr > 0:
        curr -= cost
        cost = barn_info[0] - (total - curr) // barn_info[1]
        day += 1
    print(day)
    
    barn_info = tuple(map(int, input().split()))
