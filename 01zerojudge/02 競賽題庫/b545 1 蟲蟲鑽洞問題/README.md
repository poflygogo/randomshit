## 解題紀錄

### v1-1 NA(score:80%)

```
#1: 20% WA (line:5)
您的答案為: 2 4
正確答案為: 4 4

#4: 20% RE (code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15605586_b545/code_15605586.py", line 49, in 
    main()
  File "/15605586_b545/code_15605586.py", line 44, in main
    result = worm(row, col, graph)
  File "/15605586_b545/code_15605586.py", line 2, in worm
    curr_r, curr_c = find_first_hole(max_row, max_col, graph)
TypeError: 'NoneType' object is not iterable
```

> WTF??? NoneType??? 函數沒找到僅與一個 `*` 相鄰的 `*` ??

### v1-2 NA(score:80%)

- 修正函數 `find_first_hole` 的邏輯，現在能正確尋找合適的起點了

### v1-3 AC(20ms, 3.5MB)

- 再次修正函數 `find_first_hole` 的邏輯，現在能保證該函數返回的一定是 `*` 的位置
