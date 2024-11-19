# -*- encoding: utf-8 -*-
# python 3.12
# UVa 13055 Inception
# ZeroJudge k302


stack = []
for _ in range(int(input())):
    action = input().rstrip().split()
    
    if action[0] == 'Sleep':
        stack.append(action[1])
    
    elif action[0] == 'Kick':
        if stack:
            del stack[-1]
    
    else:   # if action[0] == 'Test'
        if stack:
            print(stack[-1])
        
        else:
            print('Not in a dream')
