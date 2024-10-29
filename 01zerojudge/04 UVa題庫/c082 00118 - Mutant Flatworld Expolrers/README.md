## 解題紀錄
### v1-1 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14909109_c082/code_14909109.py", line 31, in 
    print(x, y, 'NESW'[direction])
IndexError: string index out of range
```
> nani!? how?

### v1-2 WA(line:7)
```text
您的答案為: 40 0 S LOST ...略
正確答案為: 39 0 W
```
- 修正 line 31 中未重置 direction 的值的問題

### v1-3 WA(line:7)
```text
您的答案為: 40 0 W
正確答案為: 39 0 W
```
- 特判角落的狀況
> 機器人沒掉下去了，但位置......

### v1-4 AC(21ms, 3.4MB)
- 重寫墜落判定條件，不再紀錄方位資訊，僅在可能墜落後檢查是否曾在同一個位置墜落

