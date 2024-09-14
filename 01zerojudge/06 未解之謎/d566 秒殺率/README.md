測資格式並非如題目所述，垃圾題


## 解題紀錄
### v1-1 NA(score:50%)
```text
#2: 25% WA(line:1)
您的答案為: 100%
正確答案為: 0%

#3: 25% RE(code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14502850_d566/code_14502850.py", line 17, in 
    result = sum(1 for i in data.values() if i[1]) / sum(1 for i in data if data[i][0]) * 100
ZeroDivisionError: division by zero
```
> 居然還有除以 0 的狀況......我聽說題目已經保證一定有人 AC 了呀.......

### v1-2 NA(score:50%)
- 修改保存資料的方式
> 報錯內容和 v1-1 相同

> 找到問題了，題目沒有看清楚，越靠前的測資其實是越晚

### v1-3 NA(score:75%)
```text
#3: 25% RE(code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14502850_d566/code_14502850.py", line 17, in 
    result = sum(1 for i in data.values() if i[1]) / sum(1 for i in data if data[i][0]) * 100
ZeroDivisionError: division by zero
```
- 修正判斷是否秒殺的條件
> 怎麼還是除以 0 ? 題目騙人? 但有進步就好

### v1-4-1 NA(score:75%)
- 調整資料讀取的方式
> bruh wtf 這個 0 是哪來的?

### v1-4-2 NA(score:75%)
- 調整資料讀取的方式