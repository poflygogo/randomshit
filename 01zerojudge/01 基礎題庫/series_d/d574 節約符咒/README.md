> 輸入格式不符合題意，多年前早有人回報，卻依然沒有被修正，垃圾題

## 解題紀錄
### v1-1 NA(score:25%)
```text
#0: 20% WA (line:1)
您的答案為: 5a5b5c2a2ba
正確答案為: 5a5b5c2a2b1a


#2: 15% WA (line:1)
您共輸出 0 行。
```
> 沒看懂錯哪......

### v1-2 NA(score:85%)
- 修正輸出格式，當原始資料長度比處理過的資料還精簡時，就輸出原始資料
```text
#2: 15% RE (code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14663221_d574/code_14663221.py", line 6, in 
    length1 = int(length1.rstrip())
ValueError: invalid literal for int() with base 10: '1000 swliqvtenwroxqowkwpamxbrqvjbctykjbkxyoiffrvkefqcnyibxbakgenbyzjoqligkccccoxsgdlojahgumvmntivhyztphqkmzyaiiabkebskraqiiudlnqaoaylsgzzldgzjupimuedmbgcevtxlsioqzaashdtkwyxbpiaddnotcngozsjozfwfbkpsi
```
> 這是什麼意思......原本應該讀取到數字，卻讀取到其他東西? 輸入格式有問題?

### v1-3 NA(score:30%)
- 根據測資的坑，修改輸出資料處理方式
> 好氣阿......錯更多了，輸入格式到底是長怎樣????<br>
> 根據 v1-2 報錯的內容，測資提供的咒語大小也不是 1000 個字元，而是 194 個字元阿

### v1-4 AC(1.9s, 88.3MB)
- 不用 sys.stdin 了，改使用樸素的 input()
> 煩死......stdin 到底有什麼毛病? 為什麼資料讀不完???

### v1-5 AC(1.9s, 86MB)
- 修正 v1-3 的白痴 bug，int() 忘記傳入參數
