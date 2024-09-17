## 解題思路

這題需要用到堆疊 stack 的概念 

## 類題
- [c382. 加減乘除](https://zerojudge.tw/ShowProblem?problemid=c382)(簡單)
- [f698. 後序運算式求值](https://zerojudge.tw/ShowProblem?problemid=f698)(先備知識)
- [f377. 運算式轉換](https://zerojudge.tw/ShowProblem?problemid=f377)(先備知識)
- [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)(大魔王)
- [a664. 四則運算](https://zerojudge.tw/ShowProblem?problemid=a664)(新的挑戰)
- [f640. 函數運算式求值](https://zerojudge.tw/ShowProblem?problemid=f640)(前序運算式_進階版)

## 參考資料
- [前序表達式及後序表達式(prefix expression postfix expression)](https://www.youtube.com/watch?v=ms2Lrz6l34s) | [YouTube](https://www.youtube.com/)

## 解題紀錄
### v1 NA(score:40%)
沒有處理 float 和 int 之間的轉換

### v2 AC(19ms, 3.3MB)

### v3 AC(21ms, 3.6MB)
導入 sys 和 collection，分別處理輸入輸出和 stack

### v4 AC(18ms, 3.3MB)
用字典把一個函數當值使用