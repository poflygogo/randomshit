# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge o922. 年貨大街 (Market)
# 2024-11 TOI 練習賽 新手組 第二題


input()
cost = tuple(map(int, input().split()))
result = 0
x, g = map(int, input().split())
while not (g == x == 0):
    result += g * cost[x - 1]
    x, g = map(int, input().split())
print(result)
