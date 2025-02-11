# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e908. 星期幾咧


day_name = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(day_name[(day_name.index(input()) + int(input())) % 7])
