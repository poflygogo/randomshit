## 解題紀錄

### v1-1 NA(score:20%)(RE: IndexError)

```
#0: 20% AC (41ms, 3.3MB)
#1: 20% RE (code:1) IndexError: string index out of range
#2: 20% RE (code:1) IndexError: string index out of range
#3: 40% RE (code:1) IndexError: string index out of range
```

- 根據題意寫出來的初版

### v1-2 NA(score:20%)(WA)

```
#0: 20% AC (53ms, 3.3MB)
#1: 20% WA (line:2)
#2: 20% WA (line:2)
#3: 40% WA (line:2)
```

- 質疑G碼A和G碼B並不保證等長，作者在騙人，改用 `itertools.zip_longest`


### v1-3 NA(score:80%)(RE)

```
NA(score:80%)
#0: 20% RE (code:1) IndexError: string index out of range
#1: 20% AC (38ms, 3.3MB)
#2: 20% AC (1.2s, 3.4MB)
#3: 40% AC (1.1s, 3.4MB)
```

- 認為測資格式有坑，猜測真實格式應為「第一行為密碼長度(?)，之後每組測資占用2行，分別代表G碼A和G碼B」

## v1-4 AC(0.8s, 3.4MB)

- 發問後被告知測資有空白行，調整 v1-1 的讀取方式
