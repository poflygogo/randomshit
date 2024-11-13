# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11185 Ternary
# ZeroJudge d318

while True:
    n = int(input())
    if n < 0:
        exit()
    
    result = []
    while n >= 3:
        result.append(n % 3)
        n //= 3
    
    result.append(n)
    result.reverse()
    print(*result, sep='')
