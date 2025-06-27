# -*- encoding: utf-8 -*-
# python 3.12
# UVa 00602 What Day Is It?
# ZeroJudge c069

from calendar import day_name, month_name


def is_leap(y: int) -> bool:
    # Gregorian rule in USA(after 1752)
    if y > 1752:
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    # Julian rule
    else:
        return y % 4 == 0


def mon_days(y: int, m: int) -> int:
    if m in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if m in {4, 6, 9, 11}:
        return 30
    return 29 if is_leap(y) else 28


def is_valid(m: int, d: int, y: int) -> bool:
    if not (0 < m <= 12):
        return False
    if not 0 < d <= mon_days(y, m):
        return False
    if y == 1752 and m == 9 and 2 < d < 14:
        return False
    return True


month, day, year = map(int, input().split())
while not month == day == year == 0:
    if not is_valid(month, day, year):
        print(f"{month}/{day}/{year} is an invalid date.")
    else:
        s = 4   # 已知西元元年1月1日為週六，周六的index位置為5，但要歸零，所以-1
        s += 365 * (year - 1) + sum(is_leap(i) for i in range(4, year, 4))
        s += sum(mon_days(year, i) for i in range(1, month))
        s += day
        # 採用新歷後校正時間
        if (year > 1752) or (year == 1752 and (month > 9 or (month == 9 and day >= 14))):
            s += 10
        print(f"{month_name[month]} {day}, {year} is a {day_name[s % 7]}")
    month, day, year = map(int, input().split())
