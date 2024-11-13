# 題意解析
有一數學算式 $R=B^P\bmod M$

mod在數學中是求餘的意思，用python語法表達這公式的話就是 `R = B ** P % M`

題目會依序提供P、B、M的值，請輸出R的值作為答案，其中:
- 0 <= B <= 2147483647
- 0 <= P <= 2147483647
- 1 <= M <= 46340

> 對相當大的B、P、M請寫一個有效率的演算法來。

|範例輸入|範例輸出|
|----|----|
|3<br>18132<br>17<br><br>17<br>1765<br>3<br><br>2374859<br>3029382<br>36123|13<br>2<br>13195|

---

# 解題紀錄
### v0.1 TLE
毫不意外，沒有使用任何技巧直接硬上，目的是確認我對題意理解是否正確。

### v1 TLE
首先要先知道: `a * b % c = (a % c) * (b % c)`

用程式表示的話可做成 `((((B%M)*B)%M)*B)%M...`

不過按照這個寫法100%會TLE，畢竟P很大!

### v2 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14397133_d219/code_14397133.py", line 5, in 
    B = int(line.strip())
ValueError: invalid literal for int() with base 10: '1 0 2'
```
- 使用內建函數`pow()`處理當冪值很大時的狀況，使用快速冪算法
- 其實我沒看懂報錯的原因，這是題目裡面放了一個帶有空格的數據嗎?
- 測試時是AC(18ms, 3.3MB)

### v3 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14397217_d219/code_14397217.py", line 9, in 
    P = int(stdin.readline().strip())
ValueError: invalid literal for int() with base 10: '3 18132 17'
```
- 嘗試用try捕捉ValueError，有狀況就用replace()處理掉空格
- 啊怎麼P的值也出現空格?

### v4 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14397234_d219/code_14397234.py", line 8, in 
    M = int(stdin.readline().strip().replace(' ',''))
ValueError: invalid literal for int() with base 10: ''
```
- 直接在所有輸入後方都添加`replace()`
- 為什麼到這個階段會連數字都沒了?


### v5 WA(line:1)
```
您的答案為: 14
正確答案為: 13
```
- 將接收資料的方式從sys.stdin改成input()
- 為什麼啊???單純只是改接收資料的方式，影響這麼大?

### v6 AC(93ms, 4.1MB)
- 直接try捕捉異常，如果發生無法直接`int()`的資料，就改用`split()`解包
- 結論是測資確實有問題，實際格式並非完全如題目所述

### v7 	AC(72ms, 4.1MB)
- 變更處理資料的方式，不用try捕捉異常了
- 題目騙人啊!

### v8 RE
```text
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14397556_d219/code_14397556.py", line 11, in 
    print((B ** (P / 2) % M) * (B ** (P / 2) % M) % M)
OverflowError: (34, 'Numerical result out of range')
```
- 套用公式
  - 當P為偶數時 $ B*P \bmod M = ((B* \frac{P}{2} \bmod M) * (B* \frac{P}{2}\bmod M)) \bmod M$
  - 當P為奇數時 $ B*P \bmod M = ((B \bmod M) * (B* \frac{P}{2}\bmod M)) \bmod M$
- 數字太大了，超過計算範圍限制