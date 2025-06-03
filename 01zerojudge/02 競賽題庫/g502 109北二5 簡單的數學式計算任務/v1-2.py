# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g502. 109北二5.簡單的數學式計算任務
# 109北二區桃竹苗資訊學科能力複賽


expr = input().split('+')

for i in range(len(expr)):
    expr_temp = map(int, expr[i].split('*'))
    r = 1
    for j in expr_temp:
        r *= j
    expr[i] = r

print(sum(expr) % 100000)
