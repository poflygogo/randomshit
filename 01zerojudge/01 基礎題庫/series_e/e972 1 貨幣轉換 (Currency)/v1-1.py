# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e972. 1. 貨幣轉換 (Currency)
# 2019-05 TOI 練習賽 新手組


exchange_rate = {
    'T': 1.0,
    'U': 30.9,
    'J': 0.28,
    'E': 34.5
}
money = int(input().rstrip())
cost, currency = input().rstrip().split()
money /= exchange_rate[currency]
money -= int(cost)

if money >= 0:
    print(f'{currency} {money:.2f}')
else:
    print('No Money')
