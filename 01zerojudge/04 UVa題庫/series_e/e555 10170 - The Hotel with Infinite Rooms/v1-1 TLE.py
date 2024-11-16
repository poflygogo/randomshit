# -*- encoding: utf-8 -*-
# python 3.12
# UVa 10170 The Hotel with Infinite Rooms
# ZeroJudge e555
# 
# 暴力解 TLE


while True:
    try:
        n, target = map(int, input().split())
    
    except EOFError:
        exit()
    
    else:
        while target > n:
            target -= n
            n += 1
        
        print(n)
