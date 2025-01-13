## 解題紀錄

### v1-1 RE(code:1)

- 初版

```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15410192_d481/code_15410192.py", line 26, in 
    main()
  File "/15410192_d481/code_15410192.py", line 13, in main
    if size[0] != size[3] or size[1] != size[2] or any(i <= 0 for i in size):
IndexError: tuple index out of range
```

### v1-2 RE(code:1)

- 調整條件判斷

```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15410218_d481/code_15410218.py", line 27, in 
    main()
  File "/15410218_d481/code_15410218.py", line 13, in main
    if size and all(i > 0 for i in size) and size[0] == size[3] and size[1] == size[2]:
IndexError: tuple index out of range
```

### v2-1 AC(21ms, 3.4MB)

- 意識到前面的條件判斷是大錯特錯，修正條件判斷的邏輯
