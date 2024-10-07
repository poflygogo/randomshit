## 解題紀錄
### v1-1 AC(27ms, 3.4MB)
- 用 `itertools.product` 定位資料
### v1-2 AC(19ms, 3.4MB)
- 使用生成式取代 `itertools.product`
```py
product(range(5), range(9))
# 改成
((_i, _j) for _i in range(5) for _j in range(9))
```

### v1-3 AC(18ms, 3.4MB)
- 重置壘包資訊時，不再使用切片，而是改用 `del`
```py
state = state[-3:]
# 改成
del state[:-3]
```

### v1-4 AC(21ms, 3.4MB)
- 將資料一維化
```py
# 原本的
data = [stdin.readline().rstrip().split()[1:] for _ in range(9)]

# 略...

for i, j in ((_i, _j) for _i in range(5) for _j in range(9))

# -------
# 新的
from itertools import chain

data = [[], [], [], [], []]
for _ in range(9):
    temp = stdin.readline().rstrip().split()
    del temp[0]
    for i in range(5):
        if temp:
            data[i].append(temp.pop(0))
        else:
            break

# 略...

for item in chain(*data):
```


### v2-1 AC(22ms, 3.7MB)
- 導入 collections.deque 當成 queue 使用
### v2-2 AC(20ms, 3.3MB)
- 使用普通的 list 取代 collections.deque

### v3-1 AC(20ms, 3.4MB)
- 土法煉鋼，使用 3 個變量分別表達 3 個壘包的狀態

### v4-1 AC(20ms, 3.4MB)
- 使用位運算替代 v1-3 的計算方式，用二進制數字搭配位運算模擬壘包狀態
