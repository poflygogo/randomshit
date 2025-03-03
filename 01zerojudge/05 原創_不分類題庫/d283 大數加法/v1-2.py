# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d283. 大數加法


from sys import stdin

LIMIT = 20001
fib = [0] * LIMIT
fib[1] = 1
for i in range(2, LIMIT):
    fib[i] = fib[i - 1] + fib[i - 2]

for n in stdin:
    print(fib[int(n)])
