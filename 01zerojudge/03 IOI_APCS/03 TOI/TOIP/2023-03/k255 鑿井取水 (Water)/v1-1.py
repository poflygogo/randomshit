# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k255. 鑿井取水 (Water)
# 2023-03 TOI 練習賽 新手組


day, water = map(int, input().split())

curr = 0
for i in range(day):
    curr += water - sum(map(int, input().split()[1:]))
    if curr < 0:
        print(i + 1)
        break
else:
    print('-1')
