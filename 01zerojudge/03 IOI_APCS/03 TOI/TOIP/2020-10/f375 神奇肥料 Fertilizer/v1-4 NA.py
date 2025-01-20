# -*- encoding: utf-8 -*-
# python 3.12 
# ZeroJudge f374. 分組 Grouping
# 2020-10 TOI 練習賽 新手組


height, target, patient = map(int, input().split())
day = 1
while height < target and patient > 0:
    if day % 10 not in (0, 9):
        height += height // (3 if day % 3 == 0 else 10)
        if day > 10 and day % 10 == 1 and height < target:
            patient -= 1
    day += 1

print(day if patient > 0 else 'unsalable')
