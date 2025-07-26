#

## 解題紀錄

### v1-1 NA(score: 0%) MemoryError

- 初版

```text
#0 50% RE(code:1)
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/16364997_e640/code_16364997.py", line 50, in 
    main()
  File "/16364997_e640/code_16364997.py", line 38, in main
    prompt = prompt_analyzer(input())
  File "/16364997_e640/code_16364997.py", line 13, in prompt_analyzer
    result.append(s[last:])
MemoryError

#1 50% WA(line:7)
您的答案為: 對
正確答案為: 錯
```

### v1-2 NA(score: 0%)

- 將 `pattern_analyzer` 改成生成式，用執行時間換空間，不再 MLE 了

```test
#0 50% WA(line:12)
您的答案為: 錯
正確答案為: 對

#1 50% WA(line:3)
您的答案為: 對
正確答案為: 錯
```

### v1-3 NA(score: 0%)

- 修正 `pattern_analyzer` 的邏輯，當 pattern 的結尾不是 "..." 時，不再無限循環，而是正常停止產出元素。

```test
#0 50% WA(line:23)
您的答案為: 對
正確答案為: 錯

#1 50% WA(line:3)
您的答案為: 對
正確答案為: 錯
```

### v1-4 NA(score: 0%)

- 針對特定格式的測資修改 `is_valid`，這裡的特定格式是指當傳入的規則沒有 "..." 時的狀態。

```diff
- if prompt[-1] is None and last >= len(s):
+ if (item is None and last >= len(s)) or (item is not None and last < len(s)):
    return False
```

```text
#0 50% WA(line:13)
您的答案為: 錯
正確答案為: 對

#0 50% WA(line:2)
您的答案為: 錯
正確答案為: 對
```

好像更慘了 =="
