## 解題紀錄
### v1 WA

|輸入|正確答案|我的輸出|
|-|-|-|
|4 6<br>0 0 0 0 0 0<br>0 0 0 0 0 0<br>0 0 1 0 0 0<br>0 0 0 0 0 0|0 0 0 0 0 0<br>0 0 1 0 0 0<br>0 1 1 1 0 0<br>0 0 1 0 0 0|0 2 3 0 0 0<br>0 2 3 0 0 0<br>0 2 3 0 0 0<br>0 2 3 0 0 0|

問題出在這一行
```python
danger = [[0] * num_column] * num_row
```
最一開始生成 danger 陣列的方式不恰當，導致後續修改該陣列時牽一髮而動全身，得到了不期望的結果。

應改用列表生成式 list comprehension 生成陣列。
```py
danger = [[0 for _ in range(num_column)] for _ in range(num_row)]
```

### v2 AC (0.4s, 4.8MB)
- 時間複雜度: O(n^2)

修正問題後就正常了

### v3 AC (0.4s, 3.6MB)
- 時間複雜度: O(n^2)
嘗試使用 sys.stdin 和 sys.stdout，效率沒有增加，但占用的記憶體變少了