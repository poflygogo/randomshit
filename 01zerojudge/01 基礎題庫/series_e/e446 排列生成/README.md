## 解題紀錄
### v1 AC (16.4s, 4.6MB)
過了是過了，但看到16s還是嚇了一跳

### v2 NA (score:90%)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14409736_e446/code_14409736.py", line 7, in 
    result = '\n'.join(' '.join(map(str, line)) for line in result)
  File "/14409736_e446/code_14409736.py", line 7, in 
    result = '\n'.join(' '.join(map(str, line)) for line in result)
MemoryError
```
真是誇張的數據......，怪不得前面吃16秒

### v3 AC (12.8s, 3.4MB)
用 sys.stdout.write() 輸出的成果好多了