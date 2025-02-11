# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e908. 星期幾咧


from calendar import day_name

day_name = tuple(day_name)
day = day_name.index(input())
print(day_name[(day + int(input())) % 7])
