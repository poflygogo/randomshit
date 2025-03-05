## 解題紀錄

### v1-1 NA(score:47%)

```
#6: 4% WA (line:1)
您的答案為: ?am him m ...略
正確答案為: ?may

#7: 4% WA (line:1)
您的答案為: ?am an as at do no of on or s ...略
正確答案為: ?am an as at do no so to

#10: 5% WA (line:1)
您的答案為: ?most must twas ...略
正確答案為: ?most must

...(略)

#20: 5% TLE (3s)
Killed
```

- 判斷字串的方式有誤，我實現的實際上是「該字串重新排列組合後與目標字串的差距 <= 1」
- 效率可能也有待加強...

> 或許我不該用 counter，而是應該使用 zip 或雙指針?


### v1-2 NA(score: 90%)(TLE)

- 在 v1-1 的基礎上，加強比較字串的方式，現在會逐字比較每個字串的內容

### v1-3 NA(score: 90%)(TLE)

- 不再使用 counter()，而是直接用雙指針比較字串

> 看來需要用一些手段預處理資料 hmm，但該怎麼做呢?
