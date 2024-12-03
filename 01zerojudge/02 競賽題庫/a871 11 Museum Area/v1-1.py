# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge a871. 11. Museum Area
# HP CodeWars 2010


# 用測量員公式計算面積

while True:
    try:
        length = int(input())
    except EOFError:
        break
    else:
        data = [tuple(map(float, input().split())) for _ in range(length)]
        print(f'{abs(sum(data[i][1] * data[i - 1][0] - data[i][0] * data[i - 1][1] for i in range(length))) / 2:.2f}')
