# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge q181. 1. 等紅綠燈
# 2025-01 APCS


a, b = map(int, input().split())
n    = int(input())
stu  = map(int, input().split())

cycle = a + b
print(sum(cycle - j for j in [i % cycle for i in stu] if j >= a))
