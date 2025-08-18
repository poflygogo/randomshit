# -*- encoding: utf-8 -*-
# python 3.12
# UVa 1727 Counting Weekend Days
# ZeroJudge q890

month_days = {
    "JAN": 31,
    "FEB": 28,
    "MAR": 31,
    "APR": 30,
    "MAY": 31,
    "JUN": 30,
    "JUL": 31,
    "AUG": 31,
    "SEP": 30,
    "OCT": 31,
    "NOV": 30,
    "DEC": 31,
}

weekdays = {"SUN": 0, "MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6}


def count_weekend_days(mon: str, wee: str) -> int:
    D, W = month_days[mon], weekdays[wee]
    return (((D - 1) - (5 - W) % 7) // 7 + 1) + (((D - 1) - (6 - W) % 7) // 7 + 1)


for _ in range(int(input())):
    print(count_weekend_days(*input().split()))
