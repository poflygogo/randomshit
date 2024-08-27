## 解題思路
這題需要的先備知識: 堆疊 stack

## 類題
- [c382. 加減乘除](https://zerojudge.tw/ShowProblem?problemid=c382)(簡單)
- [f698. 後序運算式求值](https://zerojudge.tw/ShowProblem?problemid=f698)(先備知識)
- [f377. 運算式轉換](https://zerojudge.tw/ShowProblem?problemid=f377)(先備知識)
- [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)(大魔王)

## 解題紀錄
### v1 AC(33ms, 3.3MB)
先...能寫出來再說XD<br>
- 處理 stack 的部分有些囉嗦，`result.appand()`和`stack.append()`都各做了 2 次，也許該思考讓他們少一點。
- 這麼標準的 stack 應該可以用 collections 的 deque 來做

### v2 AC(28ms, 3.7MB)
- 導入 collection 的 deque，當作 stack 使用
- 修改對 stack 的操作方式