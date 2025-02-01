# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge j352. 開心農場 (Farm)
# 2022-11 TOI 練習賽 新手組


n = int(input())
rain = tuple(map(int, input().split()))
sunshine = tuple(map(int, input().split()))
require_rain, require_sun = map(int, input().split())

curr_sun, curr_rain = 0, 0
for i in range(n):
    if curr_rain >= require_rain and curr_sun >= require_sun:
        print(i + 1)
        break
    curr_rain += rain[i]
    curr_sun += sunshine[i]
else:
    if curr_rain >= require_rain and curr_sun >= require_sun:
        print(n + 1)
    else:
        print('-1')
