## 解題思路

題目的規律和數字規則無關，只是在找該數字中一共有幾個圈圈
- f ( 0 ) = 1
- f ( 1 ) = 0
- f ( 2 ) = 0
- f ( 3 ) = 0
- f ( 4 ) = 0
- f ( 5 ) = 0
- f ( 6 ) = 1
- f ( 7 ) = 0
- f ( 8 ) = 2
- f ( 9 ) = 1

注意 4 雖然有一個洞，但不是圓的，所以不算

## 解題紀錄
### v1-1 AC(84ms, 4.6MB)
- 遍歷 str 形式的數字

### v1-2 AC(0.1s, 4.6MB)
- 不斷整除 10 取得每一位數字

### v1-3 AC(80ms, 4.6MB)
- 調整 v1-1 的寫法，不再特別用一個變量接收 `num.strip()` 的結果

### v1-4 AC(0.1s, 3.3MB)
- 不再導包，直接使用 input()，遇到 EOFError 時退出循環

### v1-5 NA(score:0%)
- 把 v1-4 的 input() 替換成 next(stdin).strip()
```text
RE
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14629195_c562/code_14629195.py", line 9, in 
    }[digit] for digit in next(stdin).strip()))
StopcIteration
```

### v1-6 AC(44ms, 4.8MB)
- 使用列表生成式搭配 if 篩選數字

### v1-7 AC(44ms, 4.6MB)
- 把 v1-6 的列表生成式拆開，寫成常規的 for 循環
