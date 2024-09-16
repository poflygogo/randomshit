## 類題
- [c382. 加減乘除](https://zerojudge.tw/ShowProblem?problemid=c382)(簡單)
- [f698. 後序運算式求值](https://zerojudge.tw/ShowProblem?problemid=f698)(先備知識)
- [f377. 運算式轉換](https://zerojudge.tw/ShowProblem?problemid=f377)(先備知識)
- [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)(大魔王)
- [a664. 四則運算](https://zerojudge.tw/ShowProblem?problemid=a664)(新的挑戰)

## 解題紀錄
### v1 NA(score:60%)
```text
#1: 40% RE (code:1)

您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14430920_a664/code_14430920.py", line 31, in 
    deque.appendleft(caculate[deque.pop()](deque.popleft(), deque.popleft()))
ZeroDivisionError: integer division or modulo by zero
```
> 居然有除以 0 的情況發生......是計算錯誤嗎?

> 看其他人的討論是說數值很大，會是這個原因嗎? 印象中 python 不需要太在意這個

### v2.0 NA(score:60%)
- 修復輸出答案前若 deque 內的還有運算子時，會輸出錯誤答案的情況
- 修復當左括號並非第一個字元時，會導致程式嘗試讀取錯誤的問題
- 修復低級錯誤，優先級判斷反了
- 執行程式時只會創建一次 deque 物件，並確保每次循環結束前都會清空 deque，希望能藉此提高效率
- 尚未修復除以 0 的狀況

### v2.1 NA(score:60%)
- 以 v2.0 為基準，從使用 collection.deque 雙向棧改為使用原生的 list 作為 stack 使用
> 結果不變......錯哪了......哭阿

### v2.2 AC(28ms, 4.2MB)
- 修復當運算元並非個位數時，無法取得正確數值的問題 (使用正則表達式)
> 所以不是數字太大的問題，python本來就不需要擔心這個，真正原因是題目的運算元並非只有個位數