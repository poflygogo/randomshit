## 解題紀錄
### v1-1 NA(score:91%)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14691656_e976/code_14691656.py", line 8, in 
    'I will make it!' if int(line[1]) / int(line[2]) <= int(line[0])
IndexError: list index out of range
```
> 恩!?

### v1-2 AC(52ms, 3.4MB)
- 題目並非到 EOF 為止，而是有時候到空白行為止，有時到 EOF
