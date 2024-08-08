def leepYearCheck(year):
    """
    檢查是否是閏年
    :param year: 年分(西元年)interger
    :return: 閏年=True, 平年=False
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:return True
    else:return False

def monthDaysCheck(year, month):
    """
    檢查月份的總天數
    :param year: 哪一年的月份, 用於判斷平年或閏年 interger
    :param month: 月份 interger
    :return: 當月天數 interger
    """
    return [31, 28 + int(leepYearCheck(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month-1]

def monthDayTotal(year, month, day):
    """
    統計從該年的1月1日起至指定的日期，一共有幾天
    :param year: 年分(西元年) interger
    :param month: 月份 interger
    :param day: 日期 interger
    :return: 總天數
    """
    _days = 0
    for m in range(month):
        if m == 0:continue
        else:
            _days += monthDaysCheck(year, m)
    return _days + day

def diffYearDays(ya, ma, da, yb, mb, db):
    """
    統計天數差距
    其中 ya < yb
    :param ya: 年份1 interger
    :param ma: 月份1 interger
    :param da: 日期1 interger
    :param yb: 年份2 interger
    :param mb: 月份2 interger
    :param db: 日期2 interger
    :return: 天數差距 interger
    """
    _daysA = monthDayTotal(ya, ma, da)
    _daysB = 0
    while ya < yb:
        if leepYearCheck(ya): _daysB += 366
        else: _daysB += 365
        ya += 1
    return _daysB - _daysA + monthDayTotal(yb, mb, db)

while True:
    try:
        y1 ,m1, d1 = map(int, input().split())
        y2 ,m2, d2 = map(int, input().split())

        if y1 == y2:
            if m1 == m2: print(abs(d2 - d1))
            else: print(abs(monthDayTotal(y1 ,m1, d1) - monthDayTotal(y2 ,m2, d2)))
        else:
            if y1 < y2:print(diffYearDays(y1 ,m1, d1, y2 ,m2, d2))
            else:print(diffYearDays(y2 ,m2, d2, y1 ,m1, d1))
    except EOFError:break
