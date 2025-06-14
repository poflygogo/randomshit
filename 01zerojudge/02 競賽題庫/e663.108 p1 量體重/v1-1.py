# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e663. 108 p1. 量體重
# 108新北市資訊學科能力複賽


data = list(map(int, input().split()))
total_weight = sum(data) // 4

data.sort()
c = total_weight - data[9] - data[0]
e = data[8] - c
d = data[9] - e
b = data[1] - c
a = data[0] - b
print(*sorted([a, b, c, d, e]))
