"""
印出 2000-01-01 到 2999-12-31 間所有的完全平方日

完全平方日定義:
在 yyyy-mm-dd 格式的日期中
數字 yyyymmdd 可以表示為某數 n 的平方
則 yyyy-mm-dd 為完全平方日
"""

import math
import calendar
import datetime


result = []
for i in range(math.ceil(math.sqrt(20000101)), math.floor(math.sqrt(29991231))):
    date = str(i * i)
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    if (1 <= month <= 12) and (1 <= day <= calendar.monthrange(year, month)[1]):
        result.append(datetime.date(year, month, day))

print(*result, sep='\n')
