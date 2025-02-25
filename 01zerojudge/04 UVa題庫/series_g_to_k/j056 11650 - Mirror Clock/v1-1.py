# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11650 Mirror Clock
# ZeroJudge j056


for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    m += h % 12 * 60
    m = 720 - m
    h, m = divmod(m, 60)
    if h == 0:
        h = 12
    print(f'{h:02d}:{m:02d}')
