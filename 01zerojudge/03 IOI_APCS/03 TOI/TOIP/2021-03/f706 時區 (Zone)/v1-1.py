# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f706. 時區 (Zone)
# 2021-03 TOI 練習賽 新手組


hour, min, sec, offset = map(int, input().split())
min += hour * 60
min += 90 * offset
print(f'{min // 60 % 36}:{min % 60:02d}:{sec:02d}')
