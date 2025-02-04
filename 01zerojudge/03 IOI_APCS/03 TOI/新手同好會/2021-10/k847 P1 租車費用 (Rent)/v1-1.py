# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k847. P1.租車費用 (Rent)
# 2021-10 TOI 新手同好會

# 懶得建表，直接 datetime


import datetime


m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())

date1 = datetime.date(2025, m1, d1)
date2 = datetime.date(2025, m2, d2)

date2 -= date1
date2 += datetime.timedelta(1)
print(100 * (date2.days - date2.days // 10))
