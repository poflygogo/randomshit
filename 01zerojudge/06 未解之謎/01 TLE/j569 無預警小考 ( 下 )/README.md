## 解題紀錄
### v1-1 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14712514_j569/code_14712514.py", line 15, in 
    if ans.is_integer():
AttributeError: 'Fraction' object has no attribute 'is_integer'
```
> 白癡喔!!!python 3.6 的 Fraction 不支援 is_integer

### v1-2 NA(score:1%)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14712603_j569/code_14712603.py", line 7, in 
    for i in range(int(stdin.readline().rstrip())):
ValueError: invalid literal for int() with base 10: '-2827 -170 -9164'
```
> 三小啦!改成3.6版能處理的寫法，現在還要處理題目格式的問題???

### v1-3 NA(score:1%)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14712652_j569/code_14712652.py", line 10, in 
    a, b, c = map(int, stdin.readline().rstrip().split())
ValueError: not enough values to unpack (expected 3, got 1)
```
> 題目格式到底長怎樣......

### v1-4 NA(score:1%) TLE
> 應該是猜中格式了吧?

### v1-5 NA(score:1%) TLE
