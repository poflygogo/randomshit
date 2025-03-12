# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c421. pA 雲端列印


from bisect import bisect_left
from collections import deque

data = map(int, input().split())
client = deque([])
result = []

for i in data:
    if i == -2 and client:
        result.append(client.pop())
    elif i == -1 and client:
        result.append(client.popleft())
    elif i == 0:
        break
    elif i > 0:
        client.insert(bisect_left(client, i), i)

print(*result)
