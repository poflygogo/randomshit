# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h081. 1. 程式交易
# 2022-01 APCS


n, d = map(int, input().split())
stock_price_trend = tuple(map(int, input().split()))

profit = 0
x = stock_price_trend[0]
own_stock = True

for i in range(1, len(stock_price_trend)):
    if own_stock and stock_price_trend[i] >= x + d:
        profit += stock_price_trend[i] - x
        x = stock_price_trend[i]
        own_stock = False
    elif not own_stock and stock_price_trend[i] <= x - d:
        x = stock_price_trend[i]
        own_stock = True

print(profit)
