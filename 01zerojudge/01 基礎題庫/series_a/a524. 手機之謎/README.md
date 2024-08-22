## 解題紀錄
### v1 RE(code:1)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14409814_a524/code_14409814.py", line 5, in 
    data = sorted(permutations([str(i) for i in range(1, int(line.strip()) + 1)]), reverse=True)
ValueError: invalid literal for int() with base 10: ''
```
見鬼，為什麼 strip() 後就徹底變成空字串了?

### v2 RE(code:1)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14409846_a524/code_14409846.py", line 5, in 
    line = int(line.strip())
ValueError: invalid literal for int() with base 10: ''
```
又來!?

### v3 RE(code:1)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14409886_a524/code_14409886.py", line 6, in 
    line = int(input())
ValueError: invalid literal for int() with base 10: ''
```
到底是怎樣......測資裡面有空白數據嗎?

### v4 AC (71ms, 8.5MB)
得證: 測資裡面有空白數據，坑人阿!

### v5 	AC (70ms, 8.5MB)
試試看少用一點變量會不會比較好