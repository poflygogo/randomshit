## 解題紀錄
### v1-1 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
  File "/14650310_d471/code_14650310.py", line 7
    print(f'{bin(i).lstrip('0b').zfill(num)}')
                             ^
SyntaxError: invalid token
```
> wtf????

### v1-2 RE
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
  File "/14650332_d471/code_14650332.py", line 7
    print(f'{bin(i).replace('0b', '').zfill(num)}')
                              ^
SyntaxError: invalid token
```
- 改為使用 replace() 去掉多餘的字元
> python 3.6.9 到底是有什麼毛病???

### v1-3 RE
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
  File "/14650349_d471/code_14650349.py", line 7
    print(f'{str(bin(i)).lstrip('0b').zfill(num)}')
                                  ^
SyntaxError: invalid token
```
- 將 bin() 轉換成 str()
> 歧視b ???

### v1-4 AC(42ms, 3.5MB)
- 切割字串，無視前2個字元

### v1-5 AC(45ms, 3.6MB)
- 修正語法錯誤
> 原來不是版本問題，是我的問題

### v1-6 AC(43ms, 3.5MB)
- 使用位運算求 2 的平方數

### v2-1 AC(0.1s, 8MB)
- 導入 itertools.product

### v2-2 AC(0.1s, 8MB)
- 調整 product 要遍歷的資料的型態

### v3-1 WA(line:4)
- 使用 Gemini Ai 提供的遞迴解法
> 沒有按照順序輸出結果


> 那些效率更好的答案，究竟是怎麼寫的呢?
