# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q389. 113北二1a.完全平方日
# 113北二區桃竹苗資訊學科能力複賽


def is_valid(date: int):
    day = date % 100
    mon = date % 10000 // 100
    mon_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if 1 <= mon <= 12 and 1 <= day <= mon_day[mon - 1]:
        return True
    else:
        return False


k = 4499
n = int(input())
result = (k + n) ** 2
while not is_valid(result):
    if n > 0:
        n += 1
    else:
        n -= 1
    result = (k + n) ** 2

print(result)
