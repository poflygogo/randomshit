# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge e523. 106 彰雲嘉區複賽 - Q3 費波南希數列
# 106彰雲嘉資訊學科能力複賽


fib = [1, 1, 2, 3, 5, 8, 13]
while fib[-1] < 1000000:
    fib.append(fib[-1] + fib[-2])

for _ in range(int(input())):
    n = int(input())
    if n in set(fib):
        print(fib.index(n) + 1)
    
    else:
        print('-1')
