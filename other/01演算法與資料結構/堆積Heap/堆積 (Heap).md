# 堆積 (Heap)
堆積是一種特殊的二元樹資料結構，主要用於實現優先佇列。它滿足以下特性：
- 完全二元樹: 除了最後一層，其他層都是滿的，且最後一層的節點都靠左排列。
- 堆序性: 每個節點的值都大於或等於（最大堆）或小於等於（最小堆）其所有子節點的值。

![alt text](image.png)

## 種類
- 最小堆積 (Min Heap)：每個節點的值都小於等於其所有子節點的值，根節點為最小值。
- 最大堆積 (Max Heap)：每個節點的值都大於等於其所有子節點的值，根節點為最大值。

## 應用

- 優先佇列: 最小堆積常被用來實現優先佇列，例如任務調度、圖形算法中的 Dijkstra 算法等。
- 排序算法: 堆排序就是利用堆積來實現的一種排序算法。
- Top K 問題: 找出數據流中最大的或最小的 K 個元素。
- 資料結構: 可以用於實現各種資料結構，如堆疊、佇列等。

## 操作
- 插入: 將新元素插入到最後一個葉節點，然後向上調整（heapify up）直到滿足堆的性質。
- 刪除: 將根節點（最大值或最小值）與最後一個葉節點交換，然後向下調整（heapify down）直到滿足堆的性質。
- 查找最大值/最小值: 最大值/最小值始終位於根節點，時間複雜度為 O(1)。

## 實現
- 陣列實現: 通常使用陣列來實現堆積，可以有效利用空間。
- 連結串列實現: 雖然也可以用連結串列實現，但由於需要額外的指針，效率較低。

## 時間複雜度
- 插入: O(log n)
- 刪除: O(log n)
- 查找最大值/最小值: O(1)

## 優點
- 效率高: 插入、刪除和查找最小值/最大值的時間複雜度都較低。
- 靈活: 可以用於實現各種數據結構和算法。
- Python 提供了內建的模組: 使用方便。

## 缺點
- 空間利用率: 相較於其他資料結構，堆積的空間利用率可能不是最高。

## 範例
```py
import heapq

# 創建一個空的最小堆積
heap = []

# 插入元素
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

# 獲取最小值（即根節點）
smallest = heap[0]  # O(1)

# 刪除最小值
heapq.heappop(heap)
```

## 參考資料
- [Heap Data Structure](https://www.geeksforgeeks.org/heap-data-structure/) | [GeeksforGeeks](https://www.geeksforgeeks.org/) 2024-07-31 [2024-08-21]