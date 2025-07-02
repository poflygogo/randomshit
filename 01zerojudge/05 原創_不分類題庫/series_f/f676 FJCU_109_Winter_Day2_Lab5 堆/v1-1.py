# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge f676. FJCU_109_Winter_Day2_Lab5 堆


import heapq

heap = []
heapq.heapify(heap)
while True:
    try:
        ipt = input().split()
        if ipt[0] == 'I':
            heapq.heappush(heap, -int(ipt[1]))
        else:
            print(-heapq.heappop(heap))
    except EOFError:
        break
