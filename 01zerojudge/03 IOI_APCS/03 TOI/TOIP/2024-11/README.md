## 解題紀錄

### v1-1 NA(score: 55%)

```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15471091_o926/code_15471091.py", line 2, in 
    data = [tuple(map(int, input().split()))[1:] for i in range(n)]
  File "/15471091_o926/code_15471091.py", line 2, in 
    data = [tuple(map(int, input().split()))[1:] for i in range(n)]
MemoryError
```

### v1-2 AC(1.2s, 23.8MB)

- 調整資料讀取方式，不再一口氣讀入所有數據
