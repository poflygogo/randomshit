# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12439 February 29
# Zerojudge a468


def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def count_leap_days(m1, d1, y1, m2, d2, y2) -> int:
    mon_to_int = {
        'January':1, 'February':2, 'March':3,
        'April':4, 'May':5, 'June':6,
        'July':7, 'August':8, 'September':9,
        'October':10, 'November':11, 'December':12
    }
    m1, m2 = mon_to_int[m1], mon_to_int[m2]
    result = sum(is_leap(year) for year in range(y1, y2 + 1))
    if is_leap(y1) and m1 > 2:
        result -= 1
    if is_leap(y2) and (m2 < 2 or (m2 == 2 and d2 < 29)):
        result -= 1
    return result


def main():
    for case in range(1, int(input()) + 1):
        m1, d1, y1 = input().replace(',', '').split()
        m2, d2, y2 = input().replace(',', '').split()
        print(f'Case {case}: {count_leap_days(m1, int(d1), int(y1), m2, int(d2), int(y2))}')


if __name__ == "__main__":
    main()
