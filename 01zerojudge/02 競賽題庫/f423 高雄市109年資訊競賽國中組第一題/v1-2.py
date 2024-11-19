# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f423. 高雄市109年資訊競賽國中組第一題
# 高雄市109年資訊競賽國中組第一題


print((lambda n: (n + (n % 2 != 0)) * ((n + 1) // 2) // 2)(int(input())))
