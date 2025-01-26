# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e807. 2.降雨量統計 (Rainfall statistics)
# 2019-11 TOI 練習賽 新手組


data = [tuple(map(float, input().split())) for _ in range(7)]
print(data.index(max(data, key=sum)) + 1)

period = [sum(j[i] for j in data) for i in range(4)]
print(('morning', 'afternoon', 'night', 'early morning')[period.index(max(period))])
