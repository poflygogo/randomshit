在 python 中，當我們定義一個類對象(class)時，如果沒有傳入父類，預設就是傳入object

例如
```py
class Hello:
    def __init__(self):
        print('hello world')
```

其實就等價於
```py
class Hello(object):
    def __init__(self):
        print('hello world')
```

所以我們可以說，在一切最開始的地方，有一個最原始的類誕生了，其名為 object

```py
class object:
    # ...
```
這個類是其他所有類的父類，因為它的存在，所以 python 才擁有「一切都是物件」、「萬物皆可是目標」的邏輯存在

list 其實就是一個名為 list 的類，當我們創建 list 時，其實就是在創建一個名為 list 的類對象<br>
int 其實就是一個名為 int 的類，當我們創建 int 時，其實就是在創建一個名為 int 的類對象

......依此類推

> 一切都是物件，萬物皆可為目標