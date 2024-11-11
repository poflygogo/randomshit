# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11461 Square Numbers
# Zerojudge d186

from math import sqrt


while True:
    a, b = map(int, input().split())
    if a == b == 0:
        exit()
    
    a_sqrt, b_sqrt = sqrt(a), sqrt(b)
    total = int(b_sqrt) - int(a_sqrt) + a_sqrt.is_integer()
    print(total)
