# -*- encoding: utf-8 -*-
# python 3.12
# Zerojudge a781
# HP CodeWars 2008


while True:
    n = int(input())
    if not n:
        break

    for row in range(8):
        if row % 2 == 0:
            for _ in range(n):
                print(''.join(i * n for _ in range(4) for i in ('#', '.')))
        
        else:
            for _ in range(n):
                print(''.join(i * n for _ in range(4) for i in ('.', '#')))
    
    print()
