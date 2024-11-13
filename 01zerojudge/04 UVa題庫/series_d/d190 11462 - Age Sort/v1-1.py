# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11462 Age Sort
# ZeroJudge d190

while True:
    n = int(input())
    if not n:
        exit()
    
    print(*sorted(map(int, input().split())))
