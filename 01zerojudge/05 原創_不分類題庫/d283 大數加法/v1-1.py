# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d283. 大數加法


from sys import stdin

LIMIT = 20001
fib = [''] * LIMIT
fib[0] = '0'
fib[1] = '1'
for i in range(2, LIMIT):
    fib[i] = hex(int(fib[i - 1], 16) + int(fib[i - 2], 16))[2:]

for n in stdin:
    print(int(fib[int(n)], 16))
