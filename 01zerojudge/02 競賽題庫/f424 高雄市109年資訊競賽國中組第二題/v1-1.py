# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge f424. 高雄市109年資訊競賽國中組第二題
# 高雄市109年資訊競賽國中組第二題


def nth_num(n: int, temp: list=None):
    if temp is None:
        temp = [1, 3]
    if n <= len(temp):
        return temp[n - 1]
    return nth_num(n, temp + [sum(temp[-2:])])


print(nth_num(int(input())))
