# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12650 Dangerous Dive
# ZeroJudge e546


while True:
    try:
        volunteer_go, volunteer_back = map(int, input().split())
    
    except EOFError:
        exit()
    
    else:
        if volunteer_go == volunteer_back:
            input()
            print('*')
        
        else:
            back = set(map(int, input().split()))
            result = sorted(set(range(1, volunteer_go + 1)) - back)
            print(*result)
