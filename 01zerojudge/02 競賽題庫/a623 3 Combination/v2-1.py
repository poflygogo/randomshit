# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a623. 3. Combination
# HP CodeWars 2007


from math import comb


while True:
    try:
        print(comb(*map(int, input().split())))
    
    except EOFError:
        break
