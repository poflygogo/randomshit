# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge g798. 帶動商機 (Business)
# 2021-11 TOI 練習賽 新手組


shop_info = list(map(int, input().split()))
shop_info.pop()
day = int(input())

for _ in range(day):
    temp = shop_info.copy()
    for i in range(len(shop_info)):
        if i == 0 and shop_info[1] < shop_info[0]:
            temp[1] += shop_info[0] // 10
        elif i == len(shop_info) - 1 and shop_info[-1] > shop_info[-2]:
            temp[-2] += temp[-1] // 10
        elif 0 < i < len(shop_info) - 1:
            if shop_info[i] > shop_info[i - 1]:
                temp[i - 1] += shop_info[i] // 20
            if shop_info[i] > shop_info[i + 1]:
                temp[i + 1] += shop_info[i] // 20
    shop_info = temp

print(*shop_info)
