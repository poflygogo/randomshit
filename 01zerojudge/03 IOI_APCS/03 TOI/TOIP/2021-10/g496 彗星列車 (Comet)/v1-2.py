# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g496. 彗星列車 (Comet)
# 2021-10 TOI 練習賽 新手組


print((lambda x: int(x) + (not x.is_integer()))(int.__rtruediv__(*map(int, input().split()))))
