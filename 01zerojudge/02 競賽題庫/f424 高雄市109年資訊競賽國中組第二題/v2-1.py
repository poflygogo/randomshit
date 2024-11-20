# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f424. 高雄市109年資訊競賽國中組第二題
# 高雄市109年資訊競賽國中組第二題


n = int(input())
if n <= 2:
    print((1, 3)[n - 1])

else:
    a, b = 1, 3
    for _ in range(n - 2):
        a, b = b, a + b
    print(b)
