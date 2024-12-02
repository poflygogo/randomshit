## 解題紀錄
### v1-1 NA(score:0%)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15121774_a810/code_15121774.py", line 1, in 
    from math import lcm
ImportError
```

### v1-2 NA(score:78%)
```
#1 WA

#6 RE
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15121792_a810/code_15121792.py", line 16, in 
    b // x + b // y - b // lcm(x, y) + 
ZeroDivisionError:...
```
- 針對 python 3.6 的 math 沒有 lcm 的問題，自己寫一個 lcm

### v2-1 NA(score:88%)
- 考慮更全面的狀況: a, b 同/異號、x, y 互為彼此的倍數關係、x, y 任意值為 0

### v2-2 NA(score:88%)
- 結果同上
