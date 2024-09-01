## 解題思路
1. 將題目的中序表達式轉換成後序表達式
2. 對後序表達式進行運算求值
> 可以同步進行

## 相關的關鍵字
- 中序表達式、後序表達式、前序表達式
- 運算子優先級
- 棧(stack, queue)
- 遞迴

## 類題
- [c382. 加減乘除](https://zerojudge.tw/ShowProblem?problemid=c382)(簡單)
- [f698. 後序運算式求值](https://zerojudge.tw/ShowProblem?problemid=f698)(先備知識)
- [f377. 運算式轉換](https://zerojudge.tw/ShowProblem?problemid=f377)(先備知識)
- [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)(大魔王)
- [a664. 四則運算](https://zerojudge.tw/ShowProblem?problemid=a664)(新的挑戰)

## 解題紀錄
### v0.1 RF
- 不允許使用 eval

### v1 WA(line:3)
hmm 測資不公開，不知道什麼情況會算錯

### v2 	AC(25ms, 3.7MB)
- 修正減法運算時，數值位置不正確的問題
> 效率還有改進的空間，可以一邊轉換成後序運算式，一邊進行運算

### v3 AC(24ms, 3.7MB)
- 一邊轉換成後序，一邊進行運算
> 效率還有改進的空間

### v4 AC(21ms, 3.4MB)
- 改用 list 處理 stack，結果效率變高了，記憶體占用也變少了
> deque 真的比較有效率嗎? 還是因為數據不夠大所以效果不顯著?