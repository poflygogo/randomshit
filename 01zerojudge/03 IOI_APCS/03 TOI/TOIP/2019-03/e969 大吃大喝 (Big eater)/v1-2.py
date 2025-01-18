# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e969. 大吃大喝 (Big eater)
# 2019-03 TOI 練習賽 新手組


food_cost = (32, 55)  # apple pie, corn soup
text_food_type = ('eats an Apple pie', 'drinks a Corn soup')
money, period, flag = map(int, input().split())

if money < food_cost[flag]:
    print('Wayne can\'t eat and drink.')

time = 0
while money >= food_cost[flag]:
    money -= food_cost[flag]
    print(
        f'{time}: Wayne {text_food_type[flag]}, and now he',
        f'has {money} dollar{"s" if money > 1 else ""}.' if money > 0 else 'doesn\'t have money.'
    )
    time += period
    flag ^= 1
