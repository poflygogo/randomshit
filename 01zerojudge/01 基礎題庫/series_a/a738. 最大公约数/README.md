## 解題紀錄
### v1.0 NA(score:0%)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14443066_a738/code_14443066.py", line 4, in 
    numA, numB = map(int, line.strip().split())
ValueError: not enough values to unpack (expected 2, got 0)
```
> 什麼情況? 測資有空白行?

### v1.1 AC(18ms, 3.3MB)
- 修復當測資有空白行時會報錯的問題