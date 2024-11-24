## 解題紀錄
### v1-1 RE
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15084112_a784/code_15084112.py", line 9, in 
    idx = statement.index(' = ')
ValueError: substring not found
```
> 所以有可能出現其他的賦值語法

### v2-1 AC(18ms, 3.3MB)
- 考慮測資的賦值方式有可能為賦值運算子