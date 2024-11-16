# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f071. 2. 刮刮樂 (Lottery)
# TOI 2020-05 練習賽 新手組


num_lucky = tuple(map(int, input().split()))
num_lottery = tuple(map(int, input().split()))
num_reward = tuple(map(int, input().split()))

money = 0
flag = True
for i in range(5):
    if num_lottery[i] in num_lucky[:2]:
        money += num_reward[i]
    
    elif num_lottery[i] == num_lucky[2]:
        money -= num_reward[i]
        flag = False

if flag:
    money *= 2

print('0' if money < 0 else money)
