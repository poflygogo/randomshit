import heapq
from sys import stdin


lower = []      # Max Heap, <= median
larger = []     # Min Heap, > median

for n in stdin:
    n = int(n.rstrip())

    # 將數字添加到最大堆
    heapq.heappush(lower, -n)

    # 保持最大堆中的最大值 <= 最小堆中的最小值
    if lower and larger and -lower[0] > larger[0]:
        heapq.heappush(larger, -heapq.heappop(lower))

    # 平衡兩個堆的大小，使得 lower 的大小最多比 larger 大 1
    if len(lower) > len(larger) + 1:
        heapq.heappush(larger, -heapq.heappop(lower))
    elif len(larger) > len(lower):
        heapq.heappush(lower, -heapq.heappop(larger))

    # 求中位數
    if len(lower) > len(larger):
        print(-lower[0])
    else:
        print((-lower[0] + larger[0]) // 2)
