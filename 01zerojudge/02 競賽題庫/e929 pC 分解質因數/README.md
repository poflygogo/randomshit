2015大學學測推甄申請二階

## 解題紀錄
### v1-1 NA(score:0%)
```
RE
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
  File "/14862593_e929/code_14862593.py", line 21
    print(f'{num} = {' * '.join(str(i) if factors[i] == 1 else f"{i}^{factors[i]}" for i in factors)}')
         ^
SyntaxError: f-string: expecting '}'
```

> python 3.12 能執行，但 python 3.6 不行是嗎......

### v1-2 AC(2.7s, 3.3MB)