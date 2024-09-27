原創/不分類題庫 d578. 小涵的積木

## 解題紀錄
### v1-1 NA(score:0%)
```text
#0~8 RE
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14652515_d578/code_14652515.py", line 8, in 
    print(min(data, key=lambda x: data[x]))
ValueError: min() arg is an empty sequence

#9 TLE
Killed
```
- 導入 collections.Counter
> huh??? Counter 裡面是空的?

### v1-2 NA(score:0%)
- 修改建立 counter 物件的方式
> 還是一樣...... counter 裡面沒東西

### v1-3 NA(score:40%)
```text
#1: WA(line:1)
您的答案為: 5e23,
正確答案為: Z|mH
```
- 修正並未設置停止條件的問題
> 所以有缺的積木未必是最少的?

### v1-4 NA(score:90%)
- 修正檢查數量的方式
> 現在只剩下最後一個 TLE 不知道怎麼處理了

> 當前遇到最糟糕的狀況是 `#8 2.5s, 83.4MB`，這個處理數度顯然不夠

### v2-1 NA(score:80%)
- 調整檢查重複值的方式
  - 保存所有資料到 list 後重新排序
  - 間隔 m 個元素遍歷該 list

> 在 #8 吃 TLE 了

> 這題可以玩位運算嗎?
