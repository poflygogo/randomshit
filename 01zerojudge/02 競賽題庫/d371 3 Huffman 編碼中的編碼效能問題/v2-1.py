# -*- encoding: utf-8 -*-
# python 3.12
# ZeroJudge d371. 3. Huffman 編碼中的編碼效能問題
# 96學年度全國資訊學科能力競賽


import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)

total = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    total += a + b
    heapq.heappush(arr, a + b)

print(total)
