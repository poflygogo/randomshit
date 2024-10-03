## 解題紀錄
### v1-1 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14699038_g217/code_14699038.py", line 9, in 
    print('Yes' if max(counter.values()) <= len(data) // 2 else 'No')
ValueError:...
```

### v1-2 AC(22ms, 3.6MB)
- 調整資料讀取方式