## 解題紀錄
### v1-1 NA(score:60%)
```text
RE
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14887965_o641/code_14887965.py", line 11, in 
  File "/14887965_o641/code_14887965.py", line 11, in 
MemoryError
```
> 我想也是，當 k, m 很大時，這方式要保存的矩陣也會變很大

### v1-2 NA(score:30%)
```text
#3 TLE
```
- 調整資料保存方式，僅關注上一列的內容，那就不需要把整個矩陣都記錄起來

### v1-3 NA(score:30%)
- 根據 XOR 運算的特性減少運算量(n Xor 0 = n，結果不變)

### v1-4 NA(score:30%)
- 減少運算量: 調整計算範圍，忽略矩陣中第 k 個數字左側的數字

> 看來這條路走不通......