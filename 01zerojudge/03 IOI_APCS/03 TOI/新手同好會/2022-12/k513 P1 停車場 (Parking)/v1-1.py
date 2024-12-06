# -*- encoding: utf-8 -*-
# python 3.12
# zerojudge k513. P1.停車場 (Parking)
# 2022年12月 TOI 新手同好會


parking_lots = tuple(map(int, input().split()))
total_cars = int(input())
cars = {'s': 0, 'm': 0, 'l': 0}
for item in input().split():
    item = int(item)
    if item < 200:
        cars['s'] += 1
    elif item < 500:
        cars['m'] += 1
    else:
        cars['l'] += 1

result = 0
curr_cars = 0
for item, car_type in zip(parking_lots, 'sml'):
    curr_cars += cars[car_type]
    if curr_cars < item:
        result += curr_cars
        curr_cars = 0
    else:
        result += item
        curr_cars -= item

print(result)
