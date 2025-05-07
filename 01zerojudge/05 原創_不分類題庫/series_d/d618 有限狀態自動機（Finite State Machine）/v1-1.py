# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d618. 有限狀態自動機（Finite State Machine）


for i in range(int(input())):
    state = '1'
    text = input()
    for item in text:
        if state == '2':
            if item == '1':
                state = '1'
        elif state in ('3', '4'):
            if item in ('1', '3', '4'):
                state = item
        else:
            state = item
    print(state)
