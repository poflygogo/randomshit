# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f708. 蟲蟲危機 (Insect)
# 2021-03 TOI 練習賽 新手組


m, n = map(int, input().split())
ant = map(int, input().split())
grasshopper = map(int, input().split())
print('Yes' if m > n and sum(ant) > sum(grasshopper) else 'No')
