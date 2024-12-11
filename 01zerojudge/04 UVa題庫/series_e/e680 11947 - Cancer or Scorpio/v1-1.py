# -*- encoding: utf-8 -*-
# python 3.12
# UVa 11947 Cancer or Scorpio
# ZeroJudge e680


import datetime


for id in range(1, int(input()) + 1):
    date = input()
    date = datetime.datetime(
        year=int(date[4:]),
        month=int(date[:2]),
        day=int(date[2:4])
    )
    date += datetime.timedelta(days=7*40)
    
    day = int(str(date.month) + str(date.day).rjust(2, '0'))
    print(
        id,
        date.strftime('%m/%d/%Y'),
        'aquarius' if 121 <= day <= 219 else
        'pisces' if 220 <= day <= 320 else
        'aries' if 321 <= day <= 420 else
        'taurus' if 421 <= day <= 521 else
        'gemini' if 522 <= day <= 621 else
        'cancer' if 622 <= day <= 722 else
        'leo' if 723 <= day <= 821 else
        'virgo' if 822 <= day <= 923 else
        'libra' if 924 <= day <= 1023 else
        'scorpio' if 1024 <= day <= 1122 else
        'sagittarius' if 1123 <= day <= 1222 else
        'capricorn'
    )
