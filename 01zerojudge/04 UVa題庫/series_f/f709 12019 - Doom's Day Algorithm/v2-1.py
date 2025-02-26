# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12019 Doom's Day Algorithm
# ZeroJudge f709


# Note: 2011-01-01 is Saturday
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for i in range(2, 12):
    month_day[i] += month_day[i - 1]
week_days = ('Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday')

for _ in range(int(input())):
    m, d = map(int, input().split())
    d += month_day[m - 1]
    print(week_days[d % 7])
