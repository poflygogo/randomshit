## 解題紀錄

### v1-1 NA(score:12%)

- 初版，邏輯上完全就是錯的，沒得分很合理

### v1-2 NA(score:37%)

```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15614466_b563/code_15614466.py", line 16, in 
    result = sum(data[i][j] * (i in data[j]) for i in data for j in data[i]) // 2
  File "/15614466_b563/code_15614466.py", line 16, in 
    result = sum(data[i][j] * (i in data[j]) for i in data for j in data[i]) // 2
RuntimeError: dictionary changed size during iteration
```

- 調整邏輯判斷方式，先讀入所有資料，最後才計算有多少人符合資格

> 但為什麼這個東西會修改原始資料??? 而且不是穩定觸發，要滿足某些條件?

### v1-3 AC(21ms, 3.6MB)

- 修正 v1-1 的邏輯

### v1-4 AC(22ms, 3.6MB)

- 修正 v1-2 遍歷字典的邏輯，因為 `i in data[j]` 的 `data[j]` 如果本來並不在字典中，defaultdict 會自動添加一份新的進去，這樣就會在遍歷的過程中修改字典內容了。
