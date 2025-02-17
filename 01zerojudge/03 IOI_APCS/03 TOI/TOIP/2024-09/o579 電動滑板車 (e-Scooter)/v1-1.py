# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o579. 電動滑板車 (e-Scooter)
# 2024-09 TOI 練習賽 新手組 第二題


t = int(input())
plan1 = t * 3
plan2 = 299 + (t - 300) * (t > 300) * 3
plan3 = 699 + (t - 750) * (t > 750) * 3
print(min([plan1, plan2, plan3]))
