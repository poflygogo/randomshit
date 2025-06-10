## 解題紀錄

### v1-1 NA(score: 97%)

- 初版

```
#0: 1% RE (code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/16167181_e911/code_16167181.py", line 29, in 
    main()
  File "/16167181_e911/code_16167181.py", line 8, in main
    print(*[income(arr, x, *request[i:i + 4]) for i in range(0, len(request), 4)])
  File "/16167181_e911/code_16167181.py", line 8, in 
    print(*[income(arr, x, *request[i:i + 4]) for i in range(0, len(request), 4)])
  File "/16167181_e911/code_16167181.py", line 26, in income
    return arr[a] - arr[b] * (x1 > 0) - arr[c] * (y1 > 0) + arr[d] * (x1 > 0 and y1 > 0)
IndexError: list index out of range
```

### v1-2 AC(1.2s, 60.4MB)

- 調整答案計算方式，不偷懶不寫 if 了
