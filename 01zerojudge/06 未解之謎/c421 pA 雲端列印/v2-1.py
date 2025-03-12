# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge c421. pA 雲端列印


import heapq

data = map(int, input().split())
min_heap, max_heap = [], []
cnt = 0
result = []

for i in data:
    if i == -2 and cnt:
        result.append(-heapq.heappop(max_heap))
        cnt -= 1
    elif i == -1 and cnt:
        result.append(heapq.heappop(min_heap))
        cnt -= 1
    elif i == 0:
        break
    elif i > 0:
        heapq.heappush(min_heap, i)
        heapq.heappush(max_heap, -i)
        cnt += 1

print(*result)
