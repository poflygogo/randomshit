# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge h659. 計程車 (Taxi)
# 2022-03 TOI 練習賽 新手組


k, w, s, e = map(int, input().split())

result = 20
result += 0 if k <= 2 else (k - 2) * 5
result += w // 2 * 5

if s <= 18 and e >= 19:
    result += 185
if s <= 19 and e >= 20:
    result += 195
if s <= 20 and e >= 21:
    result += 205
if s <= 21 and e >= 22:
    result += 215
if s <= 22 and e >= 23:
    result += 225

print(result)
