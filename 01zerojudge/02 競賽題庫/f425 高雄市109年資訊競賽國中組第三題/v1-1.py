# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f425. 高雄市109年資訊競賽國中組第三題
# 高雄市109年資訊競賽國中組第三題
# 
# 測量師公式、行列式


data = [tuple(map(int, input().split())) for _ in range(3)]
print(abs(
    data[0][0] * data[1][1] - data[0][1] * data[1][0] +
    data[1][0] * data[2][1] - data[1][1] * data[2][0] +
    data[2][0] * data[0][1] - data[2][1] * data[0][0]
))
