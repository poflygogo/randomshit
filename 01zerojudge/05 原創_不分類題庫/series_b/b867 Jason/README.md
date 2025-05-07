## 解題紀錄

### v1-1 NA(score:90%)

```
您的程式被監控系統中斷，可能是程式無法正常結束所導致。
Traceback (most recent call last):
  File "/15631143_b867/code_15631143.py", line 27, in 
    main()
  File "/15631143_b867/code_15631143.py", line 22, in main
    read_data(result, {})
  File "/15631143_b867/code_15631143.py", line 17, in read_data
    read_data(root, obj)
  File "/15631143_b867/code_15631143.py", line 17, in read_data
    read_data(root, obj)
  File "/15631143_b867/code_15631143.py", line 17, in read_data
    read_data(root, obj)
  [Previous line repeated 994 more times]
  File "/15631143_b867/code_15631143.py", line 9, in read_data
    if command[0] == 'end':
RecursionError: maximum recursion depth exceeded in comparison
```

- 初版，遇到遞迴過深的問題

### v1-2 AC(32ms, 5.1MB)

- 修改遞迴條件，部分邏輯改成 while 循環避免遞迴深度過深。
