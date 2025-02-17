# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o921. 生日快樂 (Birthday)
# 2024-11 TOI 練習賽 新手組 第一題


month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, 13):
    month_day[i] += month_day[i - 1]

m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

print((month_day[m2 - 1] + d2 - month_day[m1 - 1] - d1 + 365) % 365)
