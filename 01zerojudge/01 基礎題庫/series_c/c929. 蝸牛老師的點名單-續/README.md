## 類題
- [e456. Ten little Indians](https://zerojudge.tw/ShowProblem?problemid=e456)
- [c186. 蝸牛老師的點名單](https://zerojudge.tw/ShowProblem?problemid=c186)
- [c760. 蝸牛老師的點名單 (懶憜篇)](https://zerojudge.tw/ShowProblem?problemid=c760)
- [c929. 蝸牛老師的點名單-續](https://zerojudge.tw/ShowProblem?problemid=c929)
- [c659. 連接詞](https://zerojudge.tw/ShowProblem?problemid=c659)

## 注意
題目描述有問題，實際測資並非如網頁所述

真實測資結構是這樣的

|範例輸入#1|範例輸出#1|
|---|---|
|and<br>appleandbanana|apple<br>banana|

|範例輸入#2|範例輸出#2|
|---|---|
| ,<br>baluteshih ,leo ,_alan|baluteshih<br>leo<br>_alan|



## 解題紀錄

### v1 NA(score:0%)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14398994_c929/code_14398994.py", line 5, in 
    *(input().split(mark)),
EOFError: EOF when reading a line
```
- 在很奇怪的地方斷輸入了，沒看懂

### v2 NA(score:0%)
```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14398998_c929/code_14398998.py", line 4, in 
    *(input().split(mark)),
EOFError: EOF when reading a line
```
- 以為資料是分散放的，所以不用while無限循環到EOF為止
- 還是讀取不到資料，WTF?是我對題目理解有問題嗎?

### v3 NA(score:0%)
```
未產生輸出檔。(/14399017_c929/code_14399017.out (沒有此一檔案或目錄))
```
```
執行時期未定義錯誤，code = 2
sh: 1: cannot create /14399017_c929/code_14399017.out: Directory nonexistent
```
- 感覺測資有坑，嘗試不輸出開頭(例如`範例一:`之類的東西)
- 出現奇怪的東西了，什麼叫做沒有輸出檔?sh又是什麼?

### v4 AC(28ms, 3.4MB) /	AC(19ms, 3.3MB)
- 去掉括號就可以了，but why?