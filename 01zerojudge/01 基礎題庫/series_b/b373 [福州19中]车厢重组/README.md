## 解題思路
- 排序演算法: 氣泡排序 bubble sort

## 解題紀錄
### v1 NA(score:30%)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14452502_b373/code_14452502.py", line 6, in 
    if data[j] > data[j + 1]:
IndexError: list index out of range
```
>　居然會發生這種事 hmm

### v2 AC(0.2s, 3.3MB)
> 題目有坑，題目並非只有 2 行，而是有可能會把資料都分散成好幾行，要自行合併