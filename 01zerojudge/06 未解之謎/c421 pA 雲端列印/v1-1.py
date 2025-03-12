# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c421. pA 雲端列印


from bisect import bisect_left

data = map(int, input().split())
client = []
result = []

for i in data:
    if i == -2 and client:
        result.append(client.pop())
    elif i == -1 and client:
        result.append(client.pop(0))
    elif i == 0:
        break
    elif i >= 0:
        client.insert(bisect_left(client, i), i)

print(*result)
