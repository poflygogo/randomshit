# -*- encoding: utf-8 -*-
# python 3.12 
# ZeroJudge f374. 分組 Grouping
# 2020-10 TOI 練習賽 新手組


height, target, patient = map(int, input().split())
day = 1
while height < target and patient > 0:
    if day % 3 == 0 and day % 8 not in (1, 2):
        height += height // 3
    else:
        height += height // 10
    if day > 8 and day % 8 == 3 and height < target:
        patient -= 1
    day += 1

print(day if patient > 0 else 'unsalable')
