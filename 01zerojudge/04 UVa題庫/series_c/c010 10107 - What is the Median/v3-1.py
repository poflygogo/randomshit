import heapq
from sys import stdin


class MedianFinder:
    def __init__(self):
        self.small = []     # 最大堆 (Max-Heap) 存放較小的一半數據
        self.large = []     # 最小堆 (Min-Heap) 存放較大的一半數據

    def add_num(self, num):
        """添加數字到結構中"""
        # 將數字添加到最大堆
        heapq.heappush(self.small, -num)

        # 保持最大堆中的最大值 <= 最小堆中的最小值
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # 平衡兩個堆的大小，使得 `self.small` 的大小最多比 `self.large` 大 1
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def median(self):
        """返回當前數據的中位數"""
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) // 2


numbers = MedianFinder()
for n in stdin:
    numbers.add_num(int(n.rstrip()))
    print(numbers.median())
