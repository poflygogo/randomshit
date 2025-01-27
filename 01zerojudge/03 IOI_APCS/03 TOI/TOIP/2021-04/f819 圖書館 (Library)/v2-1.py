# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f819. 圖書館 (Library)
# 2021-04 TOI 練習賽 新手組


books = [tuple(map(int, input().split())) for _ in range(int(input()))]

delay = []
punish = 0
for id, day in books:
    if day <= 100:
        continue
    delay.append(id)
    punish += 5 * (day - 100)
delay.sort()

if not delay:
    print('0')
else:
    print(*delay)
    print(punish)
