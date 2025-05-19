## 解題紀錄

### v1-1 NA(score:80%)

```
#6 WA(line:1)
您的答案為: file2022
正確答案為: File 2022
```

```
#9
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15468788_i207/code_15468788.py", line 15, in 
    data.sort(key=pattern)
TypeError: '<' not supported between instances of 'tuple' and 'str'
```

### v1-2 NA(score: 80%)

- 修正 TypeError 的問題，傳遞純字串時，會以 tuple 的形式傳遞，並使用 `float('inf')` 確保字串永遠排序在數字後
- 尚未解決檔案名稱帶空格時的排序方式。(出現這種格式時["file01", "file 01"]，有空格的在前["file 01", "file01"])
