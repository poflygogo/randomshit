## 關鍵字
- [一筆畫問題](https://zh.wikipedia.org/wiki/%E4%B8%80%E7%AC%94%E7%94%BB%E9%97%AE%E9%A2%98)
- [柯尼斯堡七橋問題](https://zh.wikipedia.org/wiki/%E6%9F%AF%E5%B0%BC%E6%96%AF%E5%A0%A1%E4%B8%83%E6%A1%A5%E9%97%AE%E9%A2%98)

## 解題紀錄

### v1-1 NA(score: 91%) MLE

- 初版，直接爆記憶體wtf???

```text
#4, #5
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/16380455_b924/code_16380455.py", line 13, in 
    a, b = map(int, scan().strip().split())
  File "/usr/lib/python3.6/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
MemoryError

#6
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/16380455_b924/code_16380455.py", line 6, in 
    for line in stdin:
MemoryError
```

### v1-2 NA(score: 91%) MLE

- 調整算法，不再 counter 統計數值，而是用 bool 標記一個元素的總數是否為奇數

還是一樣爆記憶體

### v1-3 NA(score: 94%) RE

- 自暴自棄，直接 try MemoryError，抓到就瞎猜一個答案

猜中一個，但出現新問題

```text
Traceback (most recent call last):
  File "/16380584_b924/code_16380584.py", line 16, in 
    a, b = map(int, scan().strip().split())
ValueError: too many values to unpack (expected 2)
```

怎麼會有多個數字放同一行的問題啊???

### v1-4 NA(score: 52%) TLE

- 捕捉 ValueError，遇到就隨便亂賦值

### v1-5 NA(score: 52%) TLE

- 調整算法，不再維護每個元素的 bool 狀態，而是只保存奇數

### v1-6 NA(score: 97%)

- 自暴自棄，瞎猜答案

### v1-7 AC(57ms, 39.3MB)

- 自暴自棄，瞎猜另一個答案
