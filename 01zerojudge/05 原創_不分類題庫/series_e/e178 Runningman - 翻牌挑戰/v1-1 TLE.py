# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge e178. Runningman - 翻牌挑戰

# 使用 min heap 模擬
# 但 k 太大了，這樣做會 TLE

import heapq

while True:
    try:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        heapq.heapify(arr)
        for _ in range(k):
            val = heapq.heappop(arr)
            heapq.heappush(arr, -val)
        print(sum(arr))
    except EOFError:
        break
