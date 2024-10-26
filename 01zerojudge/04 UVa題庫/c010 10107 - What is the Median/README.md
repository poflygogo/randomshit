## 解題紀錄
### v1-1 TLE
- 導入 statistics.median 計算中位數
### v2-1 AC(1.5s, 4.2MB)
- 自己實現中位數的計算(比 statistics.median 少使用 1 個 if，且不再求 `len()`)
### v2-2 TLE
- 不 sort 了，每次得到新數字時直接 insert 到對應位置(線性搜)
### v2-3 AC(61ms, 4.2MB)
- 導入 bisect，改使用二分搜尋找插入位置
### v2-4 AC(0.1s, 4.3MB)
- 自己實現二分搜，不再依賴 bisect
### v3-1 AC(70ms, 4.3MB)
- 根據 chatGPT 的建議，使用兩個 heap 管理數字
### v3-2 TLE
- 嘗試用 list 模擬 heap
### v3-3 AC(66ms, 4.3MB)
- 把 v3-1 的 class 拆解開來