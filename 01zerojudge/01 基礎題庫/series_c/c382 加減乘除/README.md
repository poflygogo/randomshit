## 類題
- [c382. 加減乘除](https://zerojudge.tw/ShowProblem?problemid=c382)(簡單)
- [f698. 後序運算式求值](https://zerojudge.tw/ShowProblem?problemid=f698)(先備知識)
- [f377. 運算式轉換](https://zerojudge.tw/ShowProblem?problemid=f377)(先備知識)
- [a017. 五則運算](https://zerojudge.tw/ShowProblem?problemid=a017)(大魔王)
- [a664. 四則運算](https://zerojudge.tw/ShowProblem?problemid=a664)(新的挑戰)
- [f640. 函數運算式求值](https://zerojudge.tw/ShowProblem?problemid=f640)(前序運算式_進階版)

## 思路

這題使用內建函數`eval()`就可以做了，然而這個被封鎖了XD。不過也合理，一般也不推薦用它，因為有資安疑慮。

所以需要做`if`條件判斷，才能決定要用什麼方式運算

## 解題紀錄
### v1 NA(score:80%)
```txt
#8
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14402955_c382/code_14402955.py", line 3, in 
    if operator == '+': print(num1 + num2)
TypeError: must be str, not int
```
```txt
#9
您的答案為: -8-8-8
正確答案為: -24
```

不懂為什麼會錯......

怎麼會有運算子被轉化成`int`

那個輸出三個解的又是什麼情況? 難道是`'-8' * 3`?

### v2 (41ms, 3.3MB), (19ms, 3.3MB)
- 修正當數字為負數時，內建函數無法識別為數字的情況