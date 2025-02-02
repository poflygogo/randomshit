# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge k253. 庫存清理 (Stock)
# 2023-03 TOI 練習賽 新手組


total: int
customer: int
price: int
discount: tuple[float]
period: int
result: int

total, customer, price = map(int, input().split())
discount = (0.5, 0.6, 0.8, 0.9)
period = total // 5
result = 0
for i in range(4):
    cnt = min(customer, period + (i == 0))
    result += int(price * discount[i]) * cnt
    customer -= cnt
    if customer <= 0:
        break

print(result)
