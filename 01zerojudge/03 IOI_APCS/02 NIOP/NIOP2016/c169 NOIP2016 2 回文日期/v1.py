def get_days(yea:int, mon:int):
    days = {1:31, 3:31, 4:30, 5:31, 6:30, 7:31,
            8:31, 9:30, 10:31, 11:30, 12:31}
    if mon != 2:
        return days[mon]
    if (yea % 400 == 0) or (yea % 100 != 0 and yea % 4 == 0):
        return 29
    else:
        return 28

date1 = input()
date2 = input()

date1_yea, date1_mon, date1_day = int(date1[:4]), int(date1[4:6]), int(date1[6:])
date2_yea, date2_mon, date2_day = int(date2[:4]), int(date2[4:6]), int(date2[6:])

cnt = 0
for year in range(date1_yea, date2_yea + 1):
    date = str(year)[::-1]
    mon = int(date[:2])
    if not (0 < mon <= 12) or (year == date1_yea and mon < date1_mon):
        continue
    day = int(date[2:])
    if 0 < day <= get_days(year, mon):
        cnt += 1
print(cnt)