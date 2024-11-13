## 解題紀錄
### v1-1 AC(1.2s, 3.3MB)

### v2-1 RE(code:1)
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14501981_d442/code_14501981.py", line 7, in 
    print(f'Case #{i}: {data[0]} is {"a Happy" if num == 1 else "an Unhappy"} number.')
IndexError: list index out of range
```
- 使用生成式計算平方和
- 調整判斷是否為 happy number 的方式
> 當 num == 1 時會出錯

### v2-2 AC(1.4s, 3.3MB)
- 修正當 num == 1 時無法正確判讀的問題
>　可讀性變好，但效率變差了 hmm

### v3-1 AC(1s, 3.3MB)
- 定義一個回傳布林值 bool 的函數處理判斷，函數體用 v1-1 的方式計算

### v3-2 AC(1.1s, 3.3MB)
- 使用 v2-1 的方式判斷

### v3-3 AC(0.8s, 3.3MB)
- 修改 v3-1 的計算方式，不再使用 list 紀錄求平方和的過程，而是直接用 int 累加