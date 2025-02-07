# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f717. 抽籤


data = tuple(map(int, input().split()))
length = len(data)
result = sum(data) % length
if result == 0:
    result = length
print(result)
