# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12019 Doom's Day Algorithm
# ZeroJudge f709


import calendar
import datetime

year = 2011
for _ in range(int(input())):
    month, day = map(int, input().split())
    print(calendar.day_name[datetime.datetime(year, month, day).weekday()])
