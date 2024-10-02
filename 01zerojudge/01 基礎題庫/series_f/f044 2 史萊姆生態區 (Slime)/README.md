2020年4月TOI練習賽新手組

## 解題思路

假設史萊姆王有 n 個

d0還沒分裂，共有 n 隻史萊姆
d1分裂出 n 隻史萊姆，共有 n + n 隻史萊姆<br>
d2分裂出 2n 隻史萊姆，共有 2n + 2n 隻史萊姆<br>
d3分裂出 4n 隻史萊姆，共有 4n + 4n 隻史萊姆<br>
...<br>
di分裂出 $2^{i-1}n$ 隻史萊姆，共有 $ 2 \cdot 2^{i-1}n$ 隻史萊姆

觀察後得知當史萊姆王有 n 隻時，經過 i 天後會出現 $2 \cdot 2^{i-1}n - 1$ 隻小史萊姆

## 解題紀錄

### v1-1 NA(score:93%)

```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/14692292_f044/code_14692292.py", line 8, in 
    f'{math.log2((slime + 1) // 2 // king_slime) + 1:.0f}'
ValueError: math domain error
```

> 什麼情況下會出現這種狀況呢...

### v1-2 NA(score:93%)

- 修改化簡答案的過程，將比例化簡後取絕對值

> 結果不變hmm

### v1-3 AC(38ms, 3.3MB)

- 調整除法規則，不再強制取整數    

### v2-1 AC(21ms, 3.3MB)

- 土法煉鋼術

> 看來數字不大
