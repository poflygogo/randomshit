# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a870. 10. List Maker
# HP CodeWars 2010


arr = []
while True:
    action = input().split()

    if action[0] == 'ADD':
        arr.append(action[1])
    
    elif action[0] == 'INSERT':
        arr.insert(arr.index(action[2]), action[1])
    
    elif action[0] == 'REMOVE':
        arr.remove(action[1])

    else: # if action[0] == 'SHOW'
        print(*arr)
        break