# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11945 Financial Management
# ZeroJudge j030


for t in range(1, int(input()) + 1):
    print(f'{t} ${sum(float(input()) for _ in range(12)) / 12:,.2f}')
