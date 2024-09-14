## 解題紀錄
### v1-1 NA(score:1%)
```text
#1: 99% RE(code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14516882_a746/code_14516882.py", line 12, in 
    n, m = map(int, line.split())
ValueError: not enough values to unpack (expected 2, got 0)
```
> 有空行?

### v1-2 
```text
#1: 99% RE(code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14516935_a746/code_14516935.py", line 15, in 
    matrix = generate_matrix(n)
  File "/14516935_a746/code_14516935.py", line 5, in generate_matrix
    out = [['|'] + [' '] * num + ['|'] for _ in range(num)]
  File "/14516935_a746/code_14516935.py", line 5, in 
    out = [['|'] + [' '] * num + ['|'] for _ in range(num)]
MemoryError
```
> 哭阿! 還有 memory error 的

### v2-1 AC(0.8s, 7.3MB)
- 先記錄可能要標記 '*' 的格子，輸出時才判斷，避免保存過大的資料
> 屎山，都是屎山

